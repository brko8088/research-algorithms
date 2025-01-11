#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMaxTeamSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY skills as parameter.
#

def findMaxTeamSize(skills):
    sortedSkills = sorted(skills)
    maxTeamSize = 0
    countingSize = 0
    previousSkill = 0
    
    print(sortedSkills)
    
    for index, skill in enumerate(sortedSkills):
        if index == 0:
            previousSkill = sortedSkills[index]
        else:
            previousSkill = sortedSkills[index - 1]
        
        if skill == previousSkill or skill == previousSkill + 1:
            countingSize = countingSize + 1
            print("countingSize " + str(countingSize) + " prev " + str(previousSkill) + " cure " + str(skill))
        else:
            maxTeamSize = countingSize if countingSize > maxTeamSize else maxTeamSize
            countingSize = 1
            
    return maxTeamSize    
        
    
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skills_count = int(input().strip())

    skills = []

    for _ in range(skills_count):
        skills_item = int(input().strip())
        skills.append(skills_item)

    result = findMaxTeamSize(skills)

    fptr.write(str(result) + '\n')

    fptr.close()
