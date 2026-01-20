num = int(input())
num = 1000 - num

changes = [500,100,50,10,5,1]
cnt = 0

for i in changes:
    if num >= i:
        cnt += num // i
        num = num % i
print(cnt)