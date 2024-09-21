import sys

n = sys.stdin.readline()

for i in range(int(n)):
  a, b = sys.stdin.readline().split()
  a = int(a)
  b = int(b)
  print(f"Case #{i+1}: {a+b}")