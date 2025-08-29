import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


class TestFunctions(unittest.TestCase):
    def test_get_files_info(self):
        # Test listing files in a directory
        result = get_files_info(directory=".", working_directory=".")
        self.assertIsInstance(result, str)

    def test_get_file_content(self):
        # Test reading file content
        result = get_file_content(file_path="main.py", working_directory=".")
        self.assertIsInstance(result, str)
        self.assertIn("import os", result)

        # Test reading non-existent file
        result = get_file_content(file_path="nonexistent.py", working_directory=".")
        self.assertIsInstance(result, str)
        self.assertIn("Error", result)

    def test_run_python_file(self):
        # Test running a python file
        result = run_python_file(file_path="main.py", args=["--verbose", "test"], working_directory=".")
        self.assertIsInstance(result, str)
        # Add more assertions to validate the output of the script

if __name__ == "__main__":
    unittest.main()