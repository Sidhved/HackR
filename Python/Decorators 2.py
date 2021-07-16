'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
'''

def print_rangoli(size):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        temp = '-'.join(alp[size-1:abs(i):-1]+alp[abs(i):size])
        print(temp.center(4*size-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)