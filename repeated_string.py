#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    st_len = len(s)
    count_a_st = 0
    for i in s:
        if i == 'a':
            count_a_st = count_a_st + 1
    
    f = n//st_len
    total = f * st_len
    if total < n:
        to_add = n - total
    else:
        to_add = 0
    
    total_a = f * count_a_st
    i = 0
    while to_add != 0:
        if s[i] == 'a':
            total_a = total_a + 1
        i = i + 1
        to_add = to_add - 1
    
    return total_a   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()