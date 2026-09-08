#!/usr/bin/env python3
"""Compare JSON locale catalogs for deterministic structural defects."""

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path


NAMED_PLACEHOLDERS = (
    re.compile(r"\{\{\s*([\w.-]+)\s*\}\}"),
    re.compile(r"(?<!\{)\{\s*([\w.-]+)(?:\s*,[^{}]+)?\}(?!\})"),
    re.compile(r"\$\{\s*([\w.-]+)\s*\}"),
    re.compile(r"%\(([\w.-]+)\)[#0 +\-]?(?:\d+|\*)?(?:\.\d+)?[a-zA-Z]"),
)
PRINTF_RE = re.compile(r"%(?!%)(?:\d+\$)?[#0 +\-]?(?:\d+|\*)?(?:\.\d+)?[a-zA-Z]")
TAG_RE = re.compile(r"<\s*(/?)\s*([A-Za-z][\w:-]*)(?:\s[^<>]*)?(/?)\s*>")
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")
MOJIBAKE = ("\ufffd", "Ã", "Â", "â€")


class DuplicateKey(ValueError):
    pass


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKey(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def flatten(value, prefix=""):
    if isinstance(value, dict):
        result = {}
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            result.update(flatten(child, path))
        return result
    if isinstance(value, list):
        result = {}
        for index, child in enumerate(value):
            result.update(flatten(child, f"{prefix}[{index}]"))
        return result
    return {prefix: value}


def named_placeholders(text):
    found = []
    for pattern in NAMED_PLACEHOLDERS:
        found.extend(pattern.findall(text))
    return Counter(found)


def printf_tokens(text):
    return Counter(PRINTF_RE.findall(text))


def tag_tokens(text):
    tokens = []
    for closing, name, self_closing in TAG_RE.findall(text):
        kind = "close" if closing else "self" if self_closing else "open"
        tokens.append((kind, name.lower()))
    return Counter(tokens)


def markdown_targets(text):
    return Counter(MD_LINK_RE.findall(text))


def balanced_braces(text):
    depth = 0
    for char in text:
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def load(path):
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle, object_pairs_hook=no_duplicate_keys)
    return flatten(data)


def issue(issues, severity, code, key):
    issues.append(f"{severity} {code} {key}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--allow-identical", action="append", default=[], metavar="KEY")
    parser.add_argument(
        "--warn-expansion",
        type=float,
        metavar="RATIO",
        help="flag target strings whose character count exceeds source by this ratio",
    )
    args = parser.parse_args()

    if args.warn_expansion is not None and args.warn_expansion <= 1:
        parser.error("--warn-expansion must be greater than 1")

    try:
        source = load(args.source)
        target = load(args.target)
    except (OSError, json.JSONDecodeError, DuplicateKey) as exc:
        print(f"CRITICAL INVALID_CATALOG {exc}", file=sys.stderr)
        return 2

    issues = []
    allowed = set(args.allow_identical)
    for key in sorted(source.keys() - target.keys()):
        issue(issues, "MAJOR", "MISSING_KEY", key)
    for key in sorted(target.keys() - source.keys()):
        issue(issues, "MAJOR", "EXTRA_KEY", key)

    for key in sorted(source.keys() & target.keys()):
        left, right = source[key], target[key]
        if type(left) is not type(right):
            issue(issues, "MAJOR", "TYPE_MISMATCH", key)
            continue
        if not isinstance(left, str):
            continue
        if left and not right:
            issue(issues, "MAJOR", "EMPTY_TARGET", key)
        if named_placeholders(left) != named_placeholders(right):
            issue(issues, "MAJOR", "PLACEHOLDER_MISMATCH", key)
        if printf_tokens(left) != printf_tokens(right):
            issue(issues, "MAJOR", "PRINTF_MISMATCH", key)
        if tag_tokens(left) != tag_tokens(right):
            issue(issues, "MAJOR", "TAG_MISMATCH", key)
        if markdown_targets(left) != markdown_targets(right):
            issue(issues, "MAJOR", "LINK_TARGET_MISMATCH", key)
        if not balanced_braces(right):
            issue(issues, "MAJOR", "UNBALANCED_BRACES", key)
        if left[:1].isspace() != right[:1].isspace() or left[-1:].isspace() != right[-1:].isspace():
            issue(issues, "MINOR", "EDGE_WHITESPACE_MISMATCH", key)
        if any(marker in right for marker in MOJIBAKE):
            issue(issues, "MAJOR", "POSSIBLE_MOJIBAKE", key)
        if right != unicodedata.normalize("NFC", right):
            issue(issues, "MINOR", "NON_NFC_UNICODE", key)
        if (
            args.warn_expansion is not None
            and len(left) >= 8
            and len(right) > len(left) * args.warn_expansion
        ):
            issue(issues, "MINOR", "TEXT_EXPANSION_REVIEW", key)
        if left == right and key not in allowed and re.search(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", left):
            issue(issues, "MINOR", "IDENTICAL_TEXT_REVIEW", key)

    if issues:
        print("\n".join(issues))
        return 1
    print(f"OK: {len(source)} locale leaves pass structural checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
