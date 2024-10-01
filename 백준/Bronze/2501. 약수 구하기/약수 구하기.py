a,b = map(int,input().split())

list = []

for i in range(1,a+1):
  if (a % i == 0):
    list.append(i)
  else:
    continue
    
if (len(list) < b):
  print(0)
else:
  print(list[b-1])