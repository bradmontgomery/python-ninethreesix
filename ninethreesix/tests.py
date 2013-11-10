from nose.tools import eq_, ok_
from password import Password


def test_init():
    p = Password()

    # Test value of default parameters
    eq_(p.num_words, 4)
    eq_(p.min_len, 3)
    eq_(p.max_len, 8)
    eq_(len(p.content), 2493082)  # should be a string of this length
    eq_(p.content.find("\n"), -1)  # should contain no newlines


def test_password():
    p = Password()
    result = p.password()
    eq_(type(result), list)
    eq_(len(result), 4)


def test_as_string():
    p = Password()
    result = p.as_string()
    eq_(type(result), str)  # should return a sring
    eq_(result.count("-"), 3)  # count the delimiters
