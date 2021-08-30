# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/12932
# 자연수 뒤집어 배열로 만들기

def solution(n):
    return list(reversed([int(c) for c in str(n)]))