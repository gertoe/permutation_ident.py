#!env python3

import itertools
import sys

argv = sys.argv
argc = len(argv)

threshold = 1024

def print_usage():
    print("""Usage:
python3 find_permutation.py <wordlist file> <word to permute>
    """)

def main():
    dictfile = argv[1] # Dictionary file/wordlist
    testword = argv[2] # string to permute ('test word')
    # load wordlist/dict file
    fp = open(dictfile, 'r')
    wordlistObject = fp.readlines()
    fp.close()
    words = set()
    # preprocess wordlist (should be lowercase)
    for word in wordlistObject:
        word = word.split()
        words.add(word[0].lower())
    # free some space
    del(wordlistObject)
    # counter for permutation list
    permcount = 0
    # compute all permutations of given string (testword)
    #permutations = [ "".join(p) for p in list(itertools.permutations(str(testword)))]
    permutations = set()
    matches = set()
    for p in itertools.permutations(str(testword)):
        pword = "".join(p).lower()
        permutations.add(pword)
        #print(pword)
        permcount += 1
        # intersect wordlist/dict with permutations to identify matches if
        # threshold reached
        if permcount >= threshold:
            #print("Threshold reached. Matching with wordlist.")
            matches = matches | (words & permutations)
            # reset permutation list and counter (matches will be recorded, either.)
            permutations.clear()
            permcount = 0
    ## ENDLOOP
    print("All matches computed (if any):")
    # intersect wordlist/dict with permutations to identify matches
    matches = matches | (words & permutations)
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

