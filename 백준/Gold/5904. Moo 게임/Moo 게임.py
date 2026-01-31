import sys
input = sys.stdin.readline


N = int(input())

def moo(total_len, center_len, n):

    if total_len == 3:
        if n == 1:
            print("m")
        else:
            print("o")
        return


    prev_len = (total_len - center_len) // 2
    

    if n <= prev_len:
        moo(prev_len, center_len - 1, n)
        

    elif n > prev_len + center_len:

        moo(prev_len, center_len - 1, n - (prev_len + center_len))
    else:

        if n - prev_len == 1:
            print("m")
        else:
            print("o")


length = 3
k = 0     

while length < N:
    k += 1
    
    
    length = 2 * length + (k + 3)

moo(length, k + 3, N)