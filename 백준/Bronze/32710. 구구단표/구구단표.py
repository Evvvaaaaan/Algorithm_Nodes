N = int(input())

found = False

for i in range(2, 10):

    for j in range(1, 10):
        if N == i or N == j or N == i * j:
            found = True
            break
    if found:
        break

print(1 if found else 0)
