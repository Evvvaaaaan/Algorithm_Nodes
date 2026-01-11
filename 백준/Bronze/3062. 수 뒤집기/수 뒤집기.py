num = int(input())

for i in range(num):
    a = str(input())
    sum = int(a)+int(a[::-1])
    for i in range(len(str(sum))):
        if(str(sum)[i] != str(sum)[::-1][i]):
            answer = "NO"
            break
        else:
            answer = "YES"
    print(answer)