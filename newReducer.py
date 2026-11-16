#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all [current_word, count] items
    results = []
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            results.append((current_word, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    for current_word, total_count in sorted(results, key=lambda result: (-result[1], result[0]))[:3]:
        print ("%s%s%d" % (current_word, separator, total_count))

if __name__ == "__main__":
    main()
