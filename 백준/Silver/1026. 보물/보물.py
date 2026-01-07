num = int(input())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

aList.sort()
bList.sort(reverse=True)
answer = 0

for i in range(num):
    answer += aList[i] * bList[i]

print(answer)