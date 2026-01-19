
form = input().strip()
splits = form.split('-')


result = sum(map(int, splits[0].split('+')))

for i in splits[1:]:
    result -= sum(map(int,i.split('+')))

print(result)