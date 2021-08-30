# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수

def solution(n):
    if n <= 1: return n
    x, y, rest = 1, 1, 0
    for i in range(n-2):
        rest = x + y
        x = y
        y = rest
    return rest % 1234567