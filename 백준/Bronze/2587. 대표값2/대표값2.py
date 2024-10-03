num_list = []
sum = 0 

for i in range(5):
  num = int(input())
  num_list.append(num)

for i in range(5):
  sum += num_list[i]

num_list.sort()


print(sum//5)
print(num_list[2])