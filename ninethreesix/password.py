import argparse
import os
import string
from random import sample
from re import findall, sub


class Password(object):
    """Creates a XKCD 936-style password using words from a word list. The
    bundled word list currently comes from the Moby Word list by Grady Ward,
    which is listed in the public domain.

    The bundled word file is COMMON.TXT, which is:

        74,550 common dictionary words (common.txt)
        A list of words in common with two or more published dictionaries.
        This gives the developer of a custom spelling checker a good
        beginning pool of relatively common words.

    For the original sources, see: http://www.gutenberg.org/ebooks/3201

    This class accepts the following parameters:

    * num_words -- the number of words that will be used to generate the
      passowrd. Default is 3.
    * min_len -- the minimum length for any word. Default is 3.
    * max_len -- the maximum length for any word. Default is 6 (big words are
      hard to remember!)

    """

    def __init__(self, num_words=3, min_len=3, max_len=6):
        self.num_words = num_words
        self.min_len = min_len
        self.max_len = max_len
        self.content = self._words()

    def _words(self):
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        word_list = os.path.join(parent_dir, "COMMON.TXT")
        content = open(word_list).read()
        return sub("\s", " ", content)

    def password(self):
        pattern = r"\b\w{{{0},{1}}}\b".format(self.min_len, self.max_len)
        words = findall(pattern, self.content)
        return sample(words, self.num_words)

    def as_string(self, delimiter="-"):
        return delimiter.join(self.password())


def unreadable_password(length=20):
    """A function to generate an unreadable password. Just because."""
    return "".join(sample(string.ascii_letters, length))


def main():
    parser = argparse.ArgumentParser(description="Options for Password")
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=3,
        help="Number of words to use in your password",
    )
    parser.add_argument(
        "-m",
        "--min",
        type=int,
        default=3,
        help="Minimum lenth of each word (default is 3)",
    )
    parser.add_argument(
        "-x",
        "--max",
        type=int,
        default=6,
        help="Maximum lenth of each word (default is 6)",
    )
    parser.add_argument(
        "-u",
        "--unreadable",
        action="store_true",
        help="Specify this to produce an unreadable password instead.",
    )
    args = parser.parse_args()

    if args.unreadable:
        print(unreadable_password())
    else:
        p = Password(num_words=args.num, min_len=args.min, max_len=args.max)
        _password = p.as_string()
        print(f"\n{_password}\n")


if __name__ == "__main__":
    main()
