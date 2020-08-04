#!env python3

import itertools
import sys

argv = sys.argv
argc = len(argv)

def print_usage():
    print("""Usage:
python3 find_permutation.py <wordlist file> <word to permute>
    """)

def main():
    dictfile = argv[1]
    testword = argv[2]
    # load wordlist/dict file
    fp = open(dictfile, 'r')
    wordlistObject = fp.readlines()
    fp.close()
    wordlist = []
    # preprocess wordlist (should be lowercase)
    for word in wordlistObject:
        word = word.split()
        word = [word[0].lower()]
        wordlist.extend(word)
    wordlist = [ w.lower() for w in wordlist ]
    # compute all permutations of given string (testword)
    permutations = [ "".join(p) for p in list(itertools.permutations(str(testword)))]
    # intersect wordlist/dict with permutations to identify matches
    matches = list(set(wordlist) & set(permutations))
    # output all matches
    for match in matches:
        print(str(match))
    sys.exit(0)

if __name__ == '__main__':
    if argc != 3:
        print_usage()
        sys.exit(1)
    else:
        main()

