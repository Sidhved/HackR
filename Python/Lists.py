'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

from os import remove


if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        op, *val = input().split()
        vl = list(map(int, val))

        if op == 'append':
            l.append(vl[0])

        elif op == 'print':
            print(l)

        elif op == 'sort':
            l = sorted(l)
        
        elif op == 'pop':
            l.pop()
        
        elif op == 'reverse':
            l.reverse()

        elif op == 'remove':
            l.remove(vl[0])
        
        elif op == 'insert':
            l.insert(vl[0], vl[1])
        