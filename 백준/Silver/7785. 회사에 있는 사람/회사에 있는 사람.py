n = int(input())
stay_person = set()

for _ in range(n):
    nm, lo = input().split()
    if lo == "enter":
        stay_person.add(nm)
    elif lo == "leave":
        stay_person.discard(nm)  # 존재하지 않으면 무시됨

# 사전 순의 역순으로 정렬하여 출력
for name in sorted(stay_person, reverse=True):
    print(name)
