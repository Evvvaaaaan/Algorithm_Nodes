a = int(input())
b = int(input())
c = int(input())

cnt = [0] * 10

answer = a*b*c
answer = str(answer)

for i in range(len(answer)):
    cnt[int(answer[i])] += 1


for i in range(10):
    print(cnt[i])