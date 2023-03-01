import unittest

from .password import Password, unreadable_password


class PasswordTestCase(unittest.TestCase):
    def test_init(self):
        p = Password()

        # Test value of default parameters
        self.assertEqual(p.num_words, 3)
        self.assertEqual(p.min_len, 3)
        self.assertEqual(p.max_len, 6)
        self.assertEqual(p.content.find("\n"), -1)  # should contain no newlines

    def test_password(self):
        p = Password()
        result = p.password()
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 3)

    def test_as_string(self):
        p = Password()
        result = p.as_string()
        self.assertEqual(type(result), str)  # should return a sring
        self.assertEqual(result.count("-"), 2)  # count the delimiters


class UnreadablePasswordTestCase(unittest.TestCase):
    def test_unreadable_password(self):
        # test the default length of the password
        self.assertEqual(len(unreadable_password()), 20)

        # Test custom length
        self.assertEqual(len(unreadable_password(length=50)), 50)

        # Assert data type
        self.assertEqual(type(unreadable_password()), str)
