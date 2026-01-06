cnum = int(input())

for _ in range(cnum):
    score = list(map(float, input().split()))
    total = 0
    avg = sum(score[1:]) / score[0]

    for s in score[1:]:
        if s > avg: 
            total += 1
    rate = total / score[0] * 100
    print(f"{rate:.3f}%")
