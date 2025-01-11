#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def getOneBits(n):
    answer = []
    total = 0
    binary = "{0:b}".format(n)
    
    i = 1
    for char in binary:
        if char == '1':
            answer.append(i)
            total = total + 1
        
        i = i + 1
    
    answer.insert(0, total)
    
    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = getOneBits(n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
