import sys
input = sys.stdin.readline

answer = []

while True:
    n = int(input())
    if n == 0:
        break
    inputL = []
    for _ in range(n):
        inputL.append(input().strip())

    inputL.sort(key=str.lower)
    answer.append(inputL[0])

for i in range(len(answer)):
    print(answer[i])