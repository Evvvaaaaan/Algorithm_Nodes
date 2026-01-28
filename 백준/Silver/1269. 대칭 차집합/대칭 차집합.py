a, b = map(int,input().split())

aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

aList = set(aList)
bList = set(bList)

aL = aList.difference(bList)
bL = bList.difference(aList)

sum = len(aL) + len(bL)
print(sum)

