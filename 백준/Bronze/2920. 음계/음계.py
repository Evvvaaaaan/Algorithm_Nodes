lst = list(map(int, input().split()))
if(all(b == a + 1 for a, b in zip(lst, lst[1:]))):
    answer = 'ascending'
elif(all(b == a - 1 for a, b in zip(lst, lst[1:]))):
    answer = 'descending'
else:
    answer = 'mixed'

print(answer)