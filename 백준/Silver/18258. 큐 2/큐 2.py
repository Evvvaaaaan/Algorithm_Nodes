import sys
from collections import deque 
queue = deque()
input = sys.stdin.readline

num = int(input())
for i in range(num):
    action = input().split()
    if(action[0] == 'push'):
        queue.append(action[1])
    elif(action[0] == 'pop'):
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif(action[0] == 'front'):
        if not queue:
            print(-1)
        else: 
            print(queue[0])
    elif(action[0] == 'back'):
        if not queue:
            print(-1)
        else: 
            print(queue[-1])
    elif(action[0] == 'size'):
        print(len(queue))
    elif(action[0] == 'empty'):
        if not queue:
            print(1)
        else:
            print(0)
