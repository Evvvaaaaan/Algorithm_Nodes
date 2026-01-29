import sys
input = sys.stdin.readline
lists = []


n = int(input())

for i in range(1, n+1):
    i = str(i)
    sum = 0
    for j in range(len(i)):
        sum += int(i[j])

    if int(i) % sum == 0:
        
        lists.append(i)

print(len(lists))




