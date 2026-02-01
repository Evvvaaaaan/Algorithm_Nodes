import sys
input = sys.stdin.readline


for i in range(3):
    n = int(input())
    sum = 0
    for j in range(n):
        s = int(input())
        sum += s
    if sum == 0:
        print('0')
    elif sum > 0:
        print('+')
    elif sum < 0:
        print('-')