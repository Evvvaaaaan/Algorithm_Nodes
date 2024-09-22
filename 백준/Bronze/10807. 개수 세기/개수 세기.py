a = int(input())
#미지의 수 한 줄로 입력받기 by list  
finds = list(map(int,input().split()))
find_number = int(input())
count = 0

for i in range(a):
  if (finds[i] == find_number):
    count += 1

print(count)