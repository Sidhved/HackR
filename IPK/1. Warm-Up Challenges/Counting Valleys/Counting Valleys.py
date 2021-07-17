# Counting Valleys

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count = 0
    level = 0
    score = []
    for i in path:
        if i == "U":
            level += 1
        elif i == "D":
            level -= 1
        score.append(level)

    for i in score:
        if (score[i-1] == None and score[i] < 0) or (score [i] == 0 and score[i+1] < 0):
            count += 1
        
    return count
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
'''

steps = int(input().strip())

path = input()

result = countingValleys(steps, path)
print(result)