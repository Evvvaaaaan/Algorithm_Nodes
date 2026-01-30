import sys
input = sys.stdin.readline



MAX = 1000001
check = [True] * MAX

for i in range(2, int(MAX ** 0.5) + 1):
    if check[i]:
        for j in range(i * i, MAX, i):
            check[j] = False

while True:
    n = int(input())
    if n == 0:
        break


    found = False

    for i in range(3, n // 2 + 1, 2):
        if check[i] and check[n - i]: 
            print(f"{n} = {i} + {n - i}")
            found = True
            break

    if not found :
        print("Goldbach's conjecture is wrong.")