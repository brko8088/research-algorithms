#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'romanizer' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def intToRoman(num):

    val = [1000, 900, 500, 400,  100, 90,   50,  40,  10,  9,    5,   4,    1 ]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV", "I"]
    
    roman_num = ''
    i = 0
    
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    
    return roman_num

def romanizer(numbers):
    result = []
    
    for number in numbers:
        result.append(intToRoman(number))
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = romanizer(numbers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
