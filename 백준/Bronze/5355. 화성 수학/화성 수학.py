num = int(input())

for i in range(num):
    caseList = list(map(str, input().split()))
    result = float(caseList[0])
    for z in range(1,len(caseList)):
        if(caseList[z] == "@"):
            result *= 3
        elif(caseList[z] == "%"):
            result += 5
        elif(caseList[z] == "#"):
            result -= 7

    print(f"{result:.2f}")

            