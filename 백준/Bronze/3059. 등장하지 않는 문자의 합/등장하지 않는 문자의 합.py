import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    used = set(s)   

    total = 0
    for c in used:
        total += ord(c)

    print(2015 - total)
