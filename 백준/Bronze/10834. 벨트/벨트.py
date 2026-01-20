M = int(input())
cCount = 0
spin = 1
for i in range(M):
    a,b,c = map(int,input().split())
    if c == 1:
        cCount += 1
    spin = spin * b // a
print(1 if cCount % 2 != 0 else 0, spin)