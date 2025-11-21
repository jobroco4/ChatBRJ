# tests.py

import unittest
from functions.run_python_file import run_python_file


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.working_directory = "calculator"

    def test_calc_instructions(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_run_calc(self):
        result = run_python_file("calculator",  "main.py", ["3 + 5"])
        print(result)

    def test_calc_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_calc_outside_dir(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)

    def test_bad_extension(self):
        result = run_python_file("calculator", "lorem.txt")
        print(result)


if __name__ == "__main__":
    unittest.main()