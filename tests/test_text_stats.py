import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from text_stats import analyse

ROOT = Path(__file__).resolve().parents[1]


class AnalyseTests(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(analyse(""), {"characters": 0, "words": 0, "lines": 0})

    def test_basic_text(self):
        self.assertEqual(analyse("Hello world"), {"characters": 11, "words": 2, "lines": 1})

    def test_unicode(self):
        self.assertEqual(analyse("Příliš žluťoučký"), {"characters": 16, "words": 2, "lines": 1})

    def test_whitespace(self):
        self.assertEqual(analyse(" \t\n"), {"characters": 3, "words": 0, "lines": 1})

    def test_blank_lines_and_trailing_newline(self):
        self.assertEqual(analyse("one\n\ntwo\n"), {"characters": 9, "words": 2, "lines": 3})

    def test_windows_line_endings(self):
        self.assertEqual(analyse("a\r\nb"), {"characters": 4, "words": 2, "lines": 2})


class CommandLineTests(unittest.TestCase):
    def run_cli(self, *args, input_text=""):
        return subprocess.run(
            [sys.executable, str(ROOT / "text_stats.py"), *args],
            input=input_text, capture_output=True, text=True, encoding="utf-8",
            timeout=10,
        )

    def test_stdin(self):
        result = self.run_cli(input_text="Hello cloud")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"characters": 11, "words": 2, "lines": 1})

    def test_utf8_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sample.txt"
            path.write_text("Ahoj světe", encoding="utf-8")
            result = self.run_cli("--file", str(path))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"characters": 10, "words": 2, "lines": 1})

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_cli("--file", str(Path(folder) / "missing.txt"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("Cannot read input:", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_invalid_utf8(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "invalid.txt"
            path.write_bytes(b"\xff")
            result = self.run_cli("--file", str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("Cannot read input:", result.stderr)


if __name__ == "__main__":
    unittest.main()
