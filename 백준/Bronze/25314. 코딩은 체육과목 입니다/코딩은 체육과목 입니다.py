n = int(input())
str = ""
for i in range(n):
  if (i % 4 == 0):
    str += "long "
print(str + "int")