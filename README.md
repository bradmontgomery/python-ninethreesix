# ninethreesix

[![version](http://img.shields.io/pypi/v/python-ninethreesix.svg?style=flat-square)](https://pypi.python.org/pypi/python-ninethreesix/) [![license](http://img.shields.io/pypi/l/python-ninethreesix.svg?style=flat-square)](https://pypi.python.org/pypi/python-ninethreesix/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/) [![PyPI download month](https://img.shields.io/pypi/dm/python-ninethreesix.svg?style=flat-square)](https://pypi.org/project/python-ninethreesix/) [![codecov](https://img.shields.io/codecov/c/github/bradmontgomery/python-ninethreesix?style=flat-square)](https://codecov.io/gh/bradmontgomery/python-ninethreesix)

**a password generator**


## installation

    pip install python-ninethreesix

## usage

It comes with a script!

    $ ninethreesix --help
    $ ninethreesix
    
    wrench-fair-fascia

Or run with uvx:

    $ uvx --from python-ninethreesix ninethreesix

From python::

    >>> from ninethreesix import Password
    >>> p = Password(num_words=3, min_len=3, max_len=6)
    >>> p.as_string()
    'whelp-word-out'

Or run the module directly::

    $ python -m ninethreesix.password

    show-sine-Troy

## what's with the name?

See: [http://xckd.com/936/](http://xckd.com/936/)


## license

The code here is available under the MIT license.


## word list

The bundled word list comes from the Moby Word list by Grady Ward, which is
listed in the public domain.

The bundled word file is COMMON.TXT, which is:

    74,550 common dictionary words (common.txt)
    A list of words in common with two or more published dictionaries.
    This gives the developer of a custom spelling checker a good
    beginning pool of relatively common words.

For the original sources, see:
[http://www.gutenberg.org/ebooks/3201](http://www.gutenberg.org/ebooks/3201).


## Development

If you want to work on this library, you can install the development requirements with `uv sync` (or `make install`).

This project supports Python 3.12, 3.13, and 3.14 (preferred).

Bug  fixes and new features can be proposed by opening a Pull Request for this repo.

### Tests

Run the test suite with `uv run pytest --cov`