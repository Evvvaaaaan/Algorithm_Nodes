a = int(input())
b = list(map(int, input().split()))
max = max(b)

avg = 0
for i in range(a):
  avg += b[i]/max*100
print(avg/a)