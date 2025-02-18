import os
import unittest

from recursive_file_search.sources.helper_functions import has_even_bytesize, is_size_less_than, is_size_more_than, has_every_vowel

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.even_file = 'even_file.txt'
        self.odd_file = 'odd_file.txt'
        self.vowel_file = 'aeiou_file.txt'
        self.non_vowel_file = 'no_vowel_file.txt'
        self.big_file = 'big_file.txt'
        self.small_file = 'small_file.txt'

        with open(self.even_file, 'wb') as f:
            f.write(b'1234')
        with open(self.odd_file, 'wb') as f:
            f.write(b'123')
        with open(self.vowel_file, 'w') as f:
            f.write('This file has all vowels: aeiou')
        with open(self.non_vowel_file, 'w') as f:
            f.write('This file has no vowels')
        with open(self.big_file, 'wb') as f:
            f.write(b'x' * 2000)
        with open(self.small_file, 'wb') as f:
            f.write(b'x' * 500)

    def tearDown(self):
        os.remove(self.even_file)
        os.remove(self.odd_file)
        os.remove(self.vowel_file)
        os.remove(self.non_vowel_file)
        os.remove(self.big_file)
        os.remove(self.small_file)

    def test_has_even_bytesize(self):
        self.assertTrue(has_even_bytesize(self.even_file))
        self.assertFalse(has_even_bytesize(self.odd_file))

    def test_has_every_vowel(self):
        self.assertTrue(has_every_vowel(self.vowel_file))
        self.assertFalse(has_every_vowel(self.non_vowel_file))

    def test_is_size_more_than(self):
        self.assertTrue(is_size_more_than(self.big_file))
        self.assertFalse(is_size_more_than(self.small_file))

    def test_is_size_less_than(self):
        self.assertTrue(is_size_less_than(self.small_file))
        self.assertFalse(is_size_less_than(self.big_file))

if __name__ == '__main__':
    unittest.main()
