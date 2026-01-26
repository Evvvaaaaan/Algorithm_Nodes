import sys
input = sys.stdin.readline

num = int(input())
numbers = sorted(list(map(int,input().split())))
x = int(input())


cnt = 0
left = 0
right = num - 1

while left < right :
    cur = numbers[left] + numbers[right]

    if cur == x:
        cnt += 1
        left +=1
        right -= 1
    elif cur < x:
        left += 1
    else:
        right -= 1
print(cnt)