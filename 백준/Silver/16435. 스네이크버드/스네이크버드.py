import sys
input = sys.stdin.readline

a,b = map(int,input().split())

height = list(map(int, input().split()))
height.sort()

for i in height:
    if i <= b:
        b += 1
print(b)