# N*M 크기의 행렬 A,B 두 행렬을 더해라 
# 2차원 행렬 입력받기 

N,M = input().split()
N = int(N)
M = int(M)

A,B = [],[]

for i in range(N):
  row = list(map(int,input().split()))
  A.append(row)

for i in range(N):
  row = list(map(int,input().split()))
  B.append(row)


for i in range(N):
  for z in range(M):
    print(A[i][z] + B[i][z], end = ' ')
  print()

