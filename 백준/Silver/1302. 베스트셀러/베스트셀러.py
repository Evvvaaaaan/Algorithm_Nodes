import sys
input = sys.stdin.readline

num = int(input())
book = {}

for _ in range(num):
    title = input().strip()

    if title in book:
        book[title] += 1
    else:
        book[title] = 1

max_cnt = max(book.values())

best_seller = []
for title, count in book.items():
    if count == max_cnt:
        best_seller.append(title)


best_seller.sort()
print(best_seller[0])
