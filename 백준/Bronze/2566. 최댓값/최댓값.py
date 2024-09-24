matrix = [] 
max = 0
rowLo,colLo = 0, 0


for i in range(9):
  row = list(map(int, input().split()))
  matrix.append(row)


for row in range(9):
  for col in range(9):
    if(matrix[row][col] >= max):
      max = matrix[row][col]
      rowLo = row + 1
      colLo = col + 1

print(max)
print(rowLo, colLo)
      

