import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    a = int(input())
    if(a%2 == 0):
        print("even")
    else:
        print("odd")