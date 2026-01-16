import sys
input = sys.stdin.readline

A,B = map(int,input().split())
N = int(input())

answer = abs(A-B)

for _ in range(N):
    fav = int(input())
    answer = min(answer, abs(fav -B) + 1)


print(answer)