# 08-03
# https://programmers.co.kr/learn/courses/30/lessons/12922
# 수박수박수
# 입력 : int
# 출력 : str

def solution(n):
    return '수박'*(n//2)+'수' if n % 2 else '수박'*(n//2)