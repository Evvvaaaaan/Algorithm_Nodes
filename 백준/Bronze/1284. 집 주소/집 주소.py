import sys
input = sys.stdin.readline

while True:
    n = input().strip()
   
    if n == '0':
        break
        
    width = 0
    
    for num in n:
        if num == '1':
            width += 2
        elif num == '0':
            width += 4
        else:
            width += 3
            

    width += len(n) + 1
    
    print(width)