# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값

def solution(s):
    l = list(map(int, s.split()))
    return ' '.join(map(str, (min(l), max(l))))