'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

i = 1 부터 n -2  --> 5
j = 1 부터 n -1  --> 6
k = j + 1 부터 n 까지  --> 7
'''

n = int(input())
z = n*(n-1)*(n-2)
print(z//6)
print(3)