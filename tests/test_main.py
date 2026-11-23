import tempfile
import unittest
from pathlib import Path

import main


class EntryTests(unittest.TestCase):
    def test_entry_is_valid_and_short(self):
        main.validate(main.ENTRY)
        self.assertLessEqual(len(main.ENTRY.encode("utf-8")), 200)
        self.assertEqual(main.DEFAULT_OUTPUT, Path("/output/entry.txt"))

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            main.validate("")

    def test_rejects_whitespace(self):
        for text in (" ", "\t", "  \u00a0  "):
            with self.assertRaises(ValueError):
                main.validate(text)

    def test_rejects_over_limit(self):
        with self.assertRaises(ValueError):
            main.validate("x" * 201)
        with self.assertRaises(ValueError):
            main.validate("\u00e9" * 101)

    def test_rejects_multiline(self):
        with self.assertRaises(ValueError):
            main.validate("one\ntwo")

    def test_writes_exact_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "nested" / "entry.txt"
            self.assertEqual(main.write_entry(target), main.ENTRY)
            self.assertEqual(target.read_bytes(), main.ENTRY.encode("utf-8"))


if __name__ == "__main__":
    unittest.main()
