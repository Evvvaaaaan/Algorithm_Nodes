import sys
input = sys.stdin.readline

n = int(input())
dict = {}
for _ in range(n):
    a,b = input().split()
    if a in dict:
        dict[a] += int(b)
    else: 
        dict[a] = int(b)

if 5 in dict.values():
    print("YES")
else:
    print("NO")