from itertools import combinations


def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for combo in combinations(nums, 3):
        sum_val = sum(combo)
        if is_prime(sum_val):
            answer += 1
            
    return answer