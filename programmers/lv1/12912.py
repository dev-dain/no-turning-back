# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
# 두 정수 사이의 합

def solution(a, b):
    if a == b: return a
    return (max(a,b) - min(a,b) + 1) * (a + b) / 2