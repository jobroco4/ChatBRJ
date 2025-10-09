import unittest
from get_files_info import get_files_info

class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info()

    def test_current(self):
        result = self.get_files_info.evaluate("calculator", ".")
        self.assertEqual(result,  f'- main.py: file_size=719 bytes, is_dir=False' + '\n' + f'- tests.py: file_size=1331 bytes, is_dir=False' + '\n' + f'- pkg: file_size=44 bytes, is_dir=True')
   
    def test_pkg(self):
        result = self.get_files_info.evaluate("calculator", "pkg")
        self.assertEqual(result, f'- calculator.py: file_size=1721 bytes, is_dir=False' + '\n' + f'- render.py: file_size=376 bytes, is_dir=False')
   
    def test_outside1(self):
        result = self.get_files_info.evaluate("calculator", "/bin")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_outside2(self):
        result = self.get_files_info.evaluate("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

if __name__ == "__main__":
    unittest.main()