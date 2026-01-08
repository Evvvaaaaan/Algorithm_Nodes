max_capacity = 0
curNum = 0
for i in range(4):
    outNum, inNum = map(int, input().split())
    curNum -= outNum
    curNum += inNum
    if curNum > max_capacity:
        max_capacity = curNum

print(max_capacity)