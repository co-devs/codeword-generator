#!/usr/bin/env python3
"""Code Word Generator

This script will provide the user with a randomly generated code word.
It requires the existence of several wordlists within the same folder in order
to make those code words.

This file can also be imported as a module and contains the following

functions:
    * random_line - returns a random line from a file
    * get_noun - returns a random noun from a file
    * get_adj -returns a random adjective from a file
    * get_verb - returns a random verb from a file
    * gen_code - combines two words and returns as a codeword
    * main - the main function of the script
"""
import random
import argparse


def random_line(xfile):
    """Gets and returns a random line from a file

    Kudos to Alex Martelli and Martijn Pieters for the Waterman's Reservoir
    Algorithm code.  Not sure that it's implemented correctly, but it works.
    https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python

    Parameters
    ----------
    xfile : str
        The file location of the file to read

    Returns
    -------
    str
        The random string from the file
    """
    line = next(xfile)
    for num, xline in enumerate(xfile, 2):
        if random.randrange(num):
            continue
        line = xline
    return line


def get_noun(nfile):
    """Gets and returns a random noun from a file

    Noun list source
    http://www.desiquintans.com/downloads/nounlist/nounlist.txt

    Parameters
    ----------
    nfile : str
        The file location of the noun wordlist

    Returns
    -------
    str
        The random noun from the file
    """

    with open(nfile) as file:
        return random_line(file).strip()


def get_adj(afile):
    """Gets and returns a random adjective from a file

    Adjectives source list
    https://www.talkenglish.com/vocabulary/top-500-adjectives.aspx

    Parameters
    ----------
    afile : str
        The file location of the adjective wordlist

    Returns
    -------
    str
        The random adjective from the file
    """
    with open(afile) as file:
        return random_line(file).strip()


def get_verb(vfile):
    """Gets and returns a random verb from a file

    Verbs source list
    https://www.linguasorb.com/english/verbs/most-common-verbs/1

    Parameters
    ----------
    nfile : str
        The file location of the verb wordlist

    Returns
    -------
    str
        The random verb from the file
    """
    with open(vfile) as file:
        return random_line(file).strip()


def gen_code(nfile, afile, vfile, delim="", style=""):
    """Gets two random words and returns them as a code word

    kudos to Asim Ihsan (https://github.com/asimihsan) for the structure
    of either two nouns or an adjective and a noun
    https://gist.github.com/asimihsan/8239189
    (n,n)
    (a,n)

    Parameters
    ----------
    nfile : str
        The file location of the noun wordlist
    afile : str
        The file location of the adjective wordlist
    vfile : str
        The file location of the verb wordlist
    delim : str
        The delimiter to be used between words
    style : str
        The style of code word

    Returns
    -------
    str
        The random code word
    """
    if style == 'nn':
        num = 9
    elif style == 'an':
        num = 6
    elif style == 'vn':
        num = 5
    else:
        num = random.randint(0, 99)
    if num % 5 > 1:
        # (n,n)
        word1 = get_noun(nfile).upper()
        word2 = get_noun(nfile).upper()
        if delim:
            code = word1 + delim + word2
        else:
            code = word1 + word2
        return code
    elif num % 5 == 1:
        # (a,n)
        word1 = get_adj(afile).upper()
        word2 = get_noun(nfile).upper()
        if delim:
            code = word1 + delim + word2
        else:
            code = word1 + word2
        return code
    else:
        # (v,n)
        word1 = get_verb(vfile).upper()
        word2 = get_noun(nfile).upper()
        if delim:
            code = word1 + delim + word2
        else:
            code = word1 + word2
        return code


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", nargs='?', default=1, type=int,
                        help="the number of codewords to print")
    parser.add_argument("-d", "--delimiter", type=str,
                        help="the delimiter to use between words")
    parser.add_argument("-s", "--style", default='',
                        choices=['nn', 'an', 'vn', ''],
                        help="generate a noun-noun style code word")
    parser.add_argument("--nounlist", default='nouns.txt', type=str,
                        help="noun wordlist file")
    parser.add_argument("--adjlist", default='adjs.txt', type=str,
                        help="adjective wordlist file")
    parser.add_argument("--verblist", default='verbs.txt', type=str,
                        help="verb wordlist file")
    args = parser.parse_args()

    for i in range(args.number):
        print(gen_code(args.nounlist, args.adjlist, args.verblist, args.delimiter,
                       args.style))


if __name__ == "__main__":
    main()
