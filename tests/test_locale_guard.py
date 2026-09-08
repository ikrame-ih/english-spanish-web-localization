import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUARD = ROOT / "scripts" / "locale_guard.py"


class LocaleGuardTests(unittest.TestCase):
    def run_guard(self, source, target, *args):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            temp = Path(directory)
            source_path = temp / "source.json"
            target_path = temp / "target.json"
            source_path.write_text(json.dumps(source, ensure_ascii=False), encoding="utf-8")
            target_path.write_text(json.dumps(target, ensure_ascii=False), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(GUARD), str(source_path), str(target_path), *args],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_valid_catalog_passes(self):
        result = self.run_guard(
            {"hello": "Hello, {name}!"},
            {"hello": "¡Hola, {name}!"},
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_key_is_major(self):
        result = self.run_guard({"one": "One", "two": "Two"}, {"one": "Uno"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("MAJOR MISSING_KEY two", result.stdout)

    def test_placeholder_drift_is_major(self):
        result = self.run_guard(
            {"hello": "Hello, {name}!"},
            {"hello": "¡Hola, {nombre}!"},
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("MAJOR PLACEHOLDER_MISMATCH hello", result.stdout)

    def test_non_nfc_and_expansion_are_flagged(self):
        result = self.run_guard(
            {"title": "Short title"},
            {"title": "Ti\u0301tulo deliberadamente mucho más largo"},
            "--warn-expansion",
            "1.4",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("MINOR NON_NFC_UNICODE title", result.stdout)
        self.assertIn("MINOR TEXT_EXPANSION_REVIEW title", result.stdout)


if __name__ == "__main__":
    unittest.main()
