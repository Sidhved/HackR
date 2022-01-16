n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]
x.sort()
count=0
length=len(x)
i=0
while i<length:
    temp=x[i]
    while length>i and x[i]-temp<=k:
        i+=1
    head=x[i-1]
    while length>i and x[i]-head<=k:
        i+=1
    count+=1
print(count)