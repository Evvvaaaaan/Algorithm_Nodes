num = int(input())
cnt = {0: 0, 1: 0}


for _ in range(num):
    x = int(input())
    cnt[x] += 1

if cnt[1] > cnt[0]:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")