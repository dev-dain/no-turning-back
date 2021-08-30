# 08-04, 08-30
# https://programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기

def solution(n):
    prime = [False, False] + [True for _ in range(n-1)]
    for i in range(2, n+1):
        if prime[i] == True:
            for j in range(i * 2, n+1, i):
                prime[j] = False
    return prime.count(True)

print(solution(10))