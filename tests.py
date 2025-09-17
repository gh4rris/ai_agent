import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_calculator(self):
        result = get_files_info("calculator", ".")
        print(result)
        # self.assertIn("- main.py:", result)
        # self.assertIn("file_size=", result)
        # self.assertIn("bytes, is_dir=False", result)
        # self.assertIn("pkg", result)
        # self.assertIn("is_dir=True", result)

    def test_pkg(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        # self.assertIn("- calculator.py", result)
        # self.assertIn("file_size=", result)
        # self.assertIn("bytes, is_dir=False", result)
        # self.assertIn("- render.py", result)

    def test_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        # self.assertEqual('Error: Cannot list "/bin" as it is outside the permitted working directory', result)

    def test_not_permitted(self):
        result = get_files_info("calculator", "../")
        print(result)
        # self.assertEqual('Error: Cannot list "../" as it is outside the permitted working directory', result)


if __name__ == "__main__":
    unittest.main()