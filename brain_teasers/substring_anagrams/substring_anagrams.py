import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def string_chunks(s, length):
    list_segments = []
    for i in range(0, len(s)-length+1):
        list_segments.append(s[i:i+length])

    return list_segments


def sort_strings(s):
    return "".join(sorted(s))


def count_pairs(list_of_strings):
    nbr_pairs = 0
    set_segment = set(list_of_strings)

    # if more packages are allowed, more efficient counter: from collections import Counter
    for element in set_segment:
        nbr_duplicates_element = list_of_strings.count(element)
        nbr_pairs_element = int(nbr_duplicates_element * (nbr_duplicates_element-1) / 2)
        nbr_pairs += nbr_pairs_element
    
    return nbr_pairs


def sherlockAndAnagrams(s):
    nbr_pairs_global = 0

    print(s)
    for length in range(1, len(s)):
        print(length)

        list_segments = string_chunks(s, length)
        print(list_segments)

        list_sorted_segments = list(map(sort_strings, list_segments))
        print(list_sorted_segments)

        nbr_pairs_global += count_pairs(list_sorted_segments)
        print(nbr_pairs_global)

        print()

    return nbr_pairs_global
    
    
# change this part to read local files
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
