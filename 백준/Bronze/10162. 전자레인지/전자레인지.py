import sys
input = sys.stdin.readline


a,b,c = 300,60,10
aCount, bCount, cCount = 0,0,0


num = int(input())


while num > 0:
    if num % 10 != 0:
        print(-1)
        break
    if a <= num:
        num -= a
        aCount += 1
    elif b <= num:
        num -= b
        bCount += 1
    elif c <= num:
        num -= c
        cCount += 1


if (num == 0):
    print(aCount, bCount, cCount)