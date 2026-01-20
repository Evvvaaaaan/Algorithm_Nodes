import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    print(2**k - 1)
