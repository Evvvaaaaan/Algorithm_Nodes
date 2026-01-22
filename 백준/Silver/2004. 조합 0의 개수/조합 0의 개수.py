def cnt(x, k):
    cnt = 0
    while x >= k:
        x //= k
        cnt += x
    return cnt

n, m = map(int, input().split())

five = cnt(n, 5) - cnt(m, 5) - cnt(n - m, 5)
two  = cnt(n, 2) - cnt(m, 2) - cnt(n - m, 2)

print(min(five, two))
