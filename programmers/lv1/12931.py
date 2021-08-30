# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/12931
# 자릿수 더하기

def solution(n):
    # result = 0
    # while n:
    #     result += n % 10
    #     n //= 10
    # return result
    return sum([int(i) for i in str(n)])