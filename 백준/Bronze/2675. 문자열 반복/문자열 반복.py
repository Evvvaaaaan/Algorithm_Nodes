a = int(input())

for i in range(a):
  b,c = input().split()
  # b = 5,  c = ['/','h','t','p']
  c = list(c)
  #len(c) = 3 , l = 0 1 2 , z = 0,1,2,3,4
  for l in range(len(c)):
    for z in range(int(b)):
      print(c[l], end = '')
  print()