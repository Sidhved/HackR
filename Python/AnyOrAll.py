'''
Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
'''
import math

n = int(input())
a = list(map(int, input().split()))

def rev(num):
    return int(num != 0) and ((num % 10) * (10**int(math.log(num, 10))) + rev(num // 10))

if all(i>=0 for i in a):
    print(any(i==rev(i) for i in a))
else:
    print(False)