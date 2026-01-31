import sys
input = sys.stdin.readline

n = int(input())
months = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    months.append([a * 100 + b, c * 100 + d])

months.sort()

l = 301 
f = 1201
idx = 0 
count = 0
max_val = 0

while l < f:
    found = False
    

    while idx < n and months[idx][0] <= l:
        if months[idx][1] > max_val:
            max_val = months[idx][1]
            found = True
        idx += 1
    

    if not found:
        print(0)
        break
    
    if max_val <= l: 
        print(0)
        break

    l = max_val 
    count += 1
    

    if l >= f:
        print(count)
        break
else:

    pass