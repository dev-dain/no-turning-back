# https://programmers.co.kr/learn/courses/30/lessons/12935
# 제일 작은 수 제거하기
# 입력 : List[int]
# 출력 : List[int]

def solution(arr):
    if len(arr) <= 1: return [-1]
    arr.remove(min(arr))
    return arr