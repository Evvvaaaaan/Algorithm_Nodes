import sys

n = sys.stdin.readline()

for i in range(int(n)):
  print(str("*"*(i+1)).rjust(int(n)))