a,b = map(int,input().split())
c = int(input())
n0 = int(input())

if((a*n0 + b)<=c*n0) and (a<=c):
    print(1)
else:
    print(0)