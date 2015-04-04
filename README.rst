ninethreesix
============

|version| |license|

a password generator


usage
-----

From python::

    >>> from ninethreesix import Password
    >>> p = Password(num_words=3, min_len=3, max_len=6)
    >>> p.as_string()
    'whelp-word-out'

Or run the module directly::

    $ python -m ninethreesix.password

    show-sine-Troy


what's with the name?
---------------------

See: `http://xckd.com/936/ <http://xckd.com/936/>`_


license
-------

The code here is available under the MIT license.


word list
---------

The bundled word list comes from the Moby Word list by Grady Ward, which is
listed in the public domain.

The bundled word file is COMMON.TXT, which is:

    74,550 common dictionary words (common.txt)
    A list of words in common with two or more published dictionaries.
    This gives the developer of a custom spelling checker a good
    beginning pool of relatively common words.

For the original sources, see:
[http://www.gutenberg.org/ebooks/3201](http://www.gutenberg.org/ebooks/3201)

.. |version| image:: http://img.shields.io/pypi/v/python-ninethreesix.svg?style=flat-square
    :alt: Current Release
    :target: https://pypi.python.org/pypi/python-ninethreesix/

.. |license| image:: http://img.shields.io/pypi/l/python-ninethreesix.svg?style=flat-square
    :alt: License
    :target: https://pypi.python.org/pypi/python-ninethreesix/
