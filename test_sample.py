import subprocess
import sys
import unittest


class SampleCliTests(unittest.TestCase):
    def test_greeting_output_with_name(self) -> None:
        result = subprocess.run(
            [sys.executable, "sample.py", "太郎"],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            result.stdout.strip(),
            "こんにちは、太郎さん！Pythonサンプルへようこそ。",
        )

    def test_help_output(self) -> None:
        result = subprocess.run(
            [sys.executable, "sample.py", "--help"],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("usage:", result.stdout)
        self.assertIn("name", result.stdout)

    def test_no_args_prints_help(self) -> None:
        result = subprocess.run(
            [sys.executable, "sample.py"],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("usage:", result.stdout)


if __name__ == "__main__":
    unittest.main()
