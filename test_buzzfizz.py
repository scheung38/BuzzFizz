import unittest
from buzzfizz import div


class MyTestCase(unittest.TestCase):
    def test_div3(self):
        self.assertEqual(div(3), [1, 2, "Buzz"])

    def test_div5(self):
        self.assertEqual(div(5), [1, 2, "Buzz", 4, "Fizz"])

    def test_div6(self):
        self.assertEqual(div(6), [1, 2, "Buzz", 4, "Fizz", "Buzz"])

    def test_div9(self):
        self.assertEqual(div(9), [1, 2, "Buzz", 4, "Fizz", "Buzz", 7, 8, "Buzz"])

    def test_div12(self):
        self.assertEqual(div(12), [1, 2, "Buzz", 4, "Fizz", "Buzz", 7, 8, "Buzz", "Fizz", 11, "Buzz"])

    def test_div15(self):
        self.assertEqual(div(15),
                         [1, 2, "Buzz", 4, "Fizz", "Buzz", 7, 8, "Buzz", "Fizz", 11, "Buzz", 13, 14, "BuzzFizz"])


if __name__ == '__main__':
    unittest.main()
