import sys
input = sys.stdin.readline

n = int(input())


for _ in range(n):
    r,e,c = map(int,input().split())
    cal = r + c
    if cal < e:
        print("advertise")
    elif cal == e: 
        print("does not matter")
    elif cal > e:
        print("do not advertise")
