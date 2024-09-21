import sys

A,B = sys.stdin.readline().split()
A = int(A)
B = int(B)
print(A+B)
while (A != 0 and B != 0):
  A,B = sys.stdin.readline().split()
  A = int(A)
  B = int(B)
  if(A == 0 and B == 0):
    break
  print(A+B)