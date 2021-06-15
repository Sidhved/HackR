'''
You are given a string .
 S contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''

S = input()
a = []
A = []
Ne = []
No = []
for i in S:
    if i.islower():
        a.append(i)
    elif i.isupper():
        A.append(i)
    elif i.isdigit():
        if int(i)%2 == 0:
            Ne.append(i)
        else:
            No.append(i)

a = sorted(a)
A = sorted(A)
No = sorted(No)
Ne = sorted(Ne)

s = ''.join(a+A+No+Ne)
print(s)