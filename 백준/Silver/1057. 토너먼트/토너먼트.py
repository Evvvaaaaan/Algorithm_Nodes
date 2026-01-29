import sys
import math
input = sys.stdin.readline


n, kim, lim = map(int, input().split())
cnt = 0 

if kim > lim:
    kim, lim = lim, kim

while n > 1:
    if kim + 1 == lim and lim % 2 == 0:
        cnt += 1
        print(cnt)
        break
    else:
        kim = math.ceil(kim/2)
        lim = math.ceil(lim/2)
        cnt += 1
        n = math.ceil(n/2)


