import sys
input = sys.stdin.readline

cnt = 0

s = str(input().strip())
stack = []



for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')

    else:
        stack.pop()
        
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)