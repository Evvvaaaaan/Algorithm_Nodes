import sys
input = sys.stdin.readline

n, s = map(int,input().split())
numbers = list(map(int, input().split()))

left = 0 
right = 0
cur = 0
min_length = 100000

while True:
    if cur >= s:
        min_length = min(min_length, right - left)
        cur -= numbers[left]
        left += 1
    elif right == n:
        break
    else:
        cur += numbers[right]
        right += 1
    
if min_length == 100000:
    print(0)
else:
    print(min_length)