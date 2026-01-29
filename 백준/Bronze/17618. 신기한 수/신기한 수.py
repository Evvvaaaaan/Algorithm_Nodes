import sys
input = sys.stdin.readline
lists = []


n = int(input())
cnt = 0

for i in range(1, n+1):
    s = str(i)
    total = 0
    
    
    for char in s:
        total += int(char)

    if i % total == 0:
        cnt += 1
        
print(cnt)