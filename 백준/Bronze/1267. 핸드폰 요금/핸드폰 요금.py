import sys
input = sys.stdin.readline

num = int(input())

numbers = list(map(int, input().split()))

yPay = 0
mPay = 0    
for i in range(num):
    z = 1
    q = 1
    while z*30 <= numbers[i]:
        z += 1
    yPay += 10*z
    while q*60 <= numbers[i]:
        q += 1
    mPay += 15*q

if(yPay < mPay):
    print("Y", yPay)
elif(mPay < yPay):
    print("M", mPay)
else:
    print("Y M", yPay)