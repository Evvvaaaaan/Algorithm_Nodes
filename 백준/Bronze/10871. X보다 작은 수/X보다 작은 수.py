a,b = input().split()
a = int(a)
b = int(b)

lists = list(map(int,input().split()))
str = ""

for i in range(a):
  if(lists[i] < b):
    print(lists[i], end= ' ')
 
