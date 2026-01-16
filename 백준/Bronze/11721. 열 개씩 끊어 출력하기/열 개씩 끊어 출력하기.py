strs = input().strip()

for i in range(len(strs)):
    print(strs[i],end='')
    if(i+1) % 10 == 0:
        print()