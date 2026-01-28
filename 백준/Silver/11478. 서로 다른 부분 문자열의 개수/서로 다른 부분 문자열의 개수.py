s = input().strip()
sLen = len(s)
sSet = set()

n = len(s)

for i in range(n):
    for j in range(i+1, n+1):
        sSet.add(s[i:j])


print(len(sSet))