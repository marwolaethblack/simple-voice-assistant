import unittest
from modules.search import searchDDG, searchGoogle, truncate_string

class TestSearch(unittest.TestCase):

    def test_truncate_string(self):
        string = "Hello People also search for"
        newString = truncate_string(string, "People also search for")
        self.assertEqual(newString, 'Hello ')

if __name__ == '__main__':
    unittest.main()