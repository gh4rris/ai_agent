import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def test_main(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
       
    def test_calculator(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_bin(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)


if __name__ == "__main__":
    unittest.main()