sumAll = []
for i in range(5):
    a = list(map(int, input().split()))
    sumAll.append(sum(a))


max_value = max(sumAll)
max_index = sumAll.index(max_value) + 1

print(max_index, max_value)