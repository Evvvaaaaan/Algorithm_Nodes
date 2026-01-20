a,b = map(int, input().split())
sum_ab = 0
lists = []
for i in range(1000):
    for j in range(i):
        lists.append(i)

for i in range(a, b+1):
    sum_ab += lists[i-1]

print(sum_ab)