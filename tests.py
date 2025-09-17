import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_main(self):
        result = run_python_file("calculator", "main.py")
        print(result)
       
    def test_calculator(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_bin(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_non_scope(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_dont_exist(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)

if __name__ == "__main__":
    unittest.main()