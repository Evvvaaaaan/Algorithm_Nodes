remainList = []
for i in range(10):
    a = int(input())
    remainList.append(a%42)

remainList = list(set(remainList))
print(len(remainList))