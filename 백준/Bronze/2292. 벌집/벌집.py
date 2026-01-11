import sys
input = sys.stdin.readline

num = int(input())

if num == 1: 
    print(1)
else:
    layer = 1      
    max_num = 1    

    while num > max_num:
        max_num += 6 * layer  
        layer += 1

    print(layer)
