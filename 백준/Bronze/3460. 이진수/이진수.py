import sys
input = sys.stdin.readline
num = int(input())

for i in range (num):
    binary = int(input())
    binary = f"{binary:b}"[::-1]


    binaryL = []
    for j in range(len(binary)):
        if binary[j] == '1':
            binaryL.append(j)
    for i in binaryL:
        print(i, end=' ')
    print()