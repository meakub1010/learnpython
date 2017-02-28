#! C:\Python\python.exe
import sys
from urllib.request import urlopen


def fetch_words(url):
    """
    Fetch a list of words from a URL.

    Args:
     url: The url of a UTF-8 text document.

    Return:
        A list of string containing the words from the document.
    """

    """
        Docstring above used as help line for the current function.
        example:
        from words import *
        help(fetch_words)
    """
    'http://sixty-north.com/c/t.txt'
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """
    print one item per line
    Args:
        items: list of iterable words
    """
    for item in items:
        print(item)


def main(url):
    """
    Print each words from a text document from an url
    Args:
        url: the url of UTF-8 text document.
    :return:
    """
    words = fetch_words(url)
    print_items(words)

'print(__name__)'
'''prints the module name once when you import this module but second time or ' \
                'later import it will not print the module name'''

if __name__ == '__main__':
    main(sys.argv[1]) # the 0th argument is the module file name.

