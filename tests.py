import unittest
from functions.get_files_info import get_file_content

class TestGetFileContent(unittest.TestCase):
    def test_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)
       
    def test_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_bin(self):
        result = get_file_content("calculator", "bin/cat")
        print(result)

    def test_not_exist(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)


if __name__ == "__main__":
    unittest.main()