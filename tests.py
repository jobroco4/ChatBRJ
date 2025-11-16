# tests.py

import unittest
from functions.get_files_info import get_files_info

get_files_info("calculator", ".")

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.working_directory = "calculator"

    def test_list_current_directory(self):
        result = get_files_info(self.working_directory, ".")
        print(result)

    def test_list_subdirectory(self):
        result = get_files_info(self.working_directory, "pkg")
        print(result)

    def test_list_non_existent_directory(self):
        result = get_files_info(self.working_directory, "/bin")
        print(result)

    def test_abs_path(self):
        result = get_files_info(self.working_directory, "../")
        print(result)


if __name__ == "__main__":
    unittest.main()