n = int(input())
arr = list(map(int, input().split()))
dict = {}
count = 0

for i in arr:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1

for i in dict:
    if dict[i] >= 2:
        count += dict[i]//2

print(count)