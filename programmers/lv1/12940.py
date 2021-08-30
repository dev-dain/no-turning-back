# 08-03
# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최대공약수와 최대공배수 구하기
# 입력 : int, int
# 출력 : int, int

def solution(n, m):
    a, b = max(n, m), min(n, m)
    while b != 0:
        a, b = b, a % b
    return [a, (n*m)/a]