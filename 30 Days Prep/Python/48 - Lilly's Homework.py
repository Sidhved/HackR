import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

n = int(input())
l = list(map(int, input().split()))

sort = sorted(l)
rev = list(reversed(l))

d = {}
for i in range(n):
    if sort[i] not in d:
        d[sort[i]] = i

swaps = 0
i = 0
while i < n:
    if sort[i] == l[i]:
        i += 1
        continue
    swaps += 1
    l[d[l[i]]], l[i] = l[i], l[d[l[i]]]
    d[sort[i]] += 1

d = {}
for i in range(n):
    if sort[i] not in d:
        d[sort[i]] = i

swaps_rev = 0
i = 0
while i < n:
    if sort[i] == rev[i]:
        i += 1
        continue
    swaps_rev += 1
    rev[d[rev[i]]], rev[i] = rev[i], rev[d[rev[i]]]
    d[sort[i]] += 1

print(min(swaps, swaps_rev))