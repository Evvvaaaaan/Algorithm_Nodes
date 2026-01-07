roomNum = input().strip()

cnt = [0] * 10

for num in roomNum:
    cnt[int(num)] += 1
six_nine = cnt[6] + cnt[9]
cnt[6] = (six_nine+1)// 2
cnt[9] = 0 

print(max(cnt))