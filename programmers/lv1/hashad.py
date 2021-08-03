# https://programmers.co.kr/learn/courses/30/lessons/12947
# 하샤드 수
# 입력 : int
# 출력 : boolean

def solution(x):
    if x < 11: return True
    return not (x % sum([int(c) for c in str(x)]))