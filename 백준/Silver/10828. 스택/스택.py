stack = []
num = int(input())

for i in range(num):
    action = input().split()
    if(action[0] == 'push'):
        stack.append(action[1])
    elif(action[0] == 'pop'):
        if not stack:
            print(-1)
        else:
            print(stack.pop())
            
    elif(action[0] == 'top'):
        if not stack:
            print(-1)
        else: 
            print(stack[-1])
    elif(action[0] == 'size'):
        print(len(stack))
    elif(action[0] == 'empty'):
        if not stack:
            print(1)
        else:
            print(0)