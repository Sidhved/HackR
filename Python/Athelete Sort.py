'''
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.
'''

# !/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter  # This was the key to solve the problem


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    ar = sorted(arr, key=itemgetter(k))

    for i in range(n):
        for j in range(m):
            print(ar[i][j], end=" ")
        print()