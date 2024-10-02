N, M = map(int, input().split())
numbers = [int(num) for num in input().split()]

max_sum = 0 

for i in range(N):
    for z in range(i + 1, N):
        for q in range(z + 1, N):
            current_sum = numbers[i] + numbers[z] + numbers[q]
            if current_sum <= M and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)
