'''
네 좌표가 주어지는데 

왼쪽 아래, 오른쪽 위 꼭짓점을 구하는 방법 : 주어진 x,y 좌표 중 


0. 가장 큰 x, 가장 큰 y 가 오른쪽 위
1. 가장 작은 x, 가장 작은 y 왼쪽 아래 
2. 가장 큰 x, 가장 작은 y 오른쪽 아래
3. 가장 작은 x, 가장 큰 y 왼쪽 위

넓이 : (2번x - 1번x) * (3번y - 1번y)
즉, 가장 큰 x - 가장 작은 x * 가장 y  - 가 작 y 
'''

n = int(input())
listX = []
listY = []
for i in range(n):
  a,b = map(int,input().split())
  listX.append(a)
  listY.append(b)

print((max(listX)-min(listX))*(max(listY)-min(listY)))