import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()


if s[0] == 'A':
    count_a = 0 
    count_b = 1 
else: 
    count_a = 1 
    count_b = 0 


for i in range(1, n):
    char = s[i]

    next_a = 0
    next_b = 0
    
    if char == 'A':

        next_a = min(count_a, count_b + 1)

        next_b = min(count_b + 1, count_a + 1)
    else:
        next_a = min(count_a + 1, count_b + 1)
        next_b = min(count_b, count_a + 1)
 
    count_a = next_a
    count_b = next_b
print(count_a)