# 첫째 줄에 문자열 개수 n개 m이 주어진다 

n, m = map(int,input().split())

f_list = set()

for _ in range(n):
  f_list.add(input())

correct = 0
for _ in range(m):
  find_word = input()
  if find_word in f_list:
    correct += 1

print(correct)