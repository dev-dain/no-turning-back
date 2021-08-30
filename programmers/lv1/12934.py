# 08-03
# https://programmers.co.kr/learn/courses/30/lessons/12934
# 정수 제곱근 판별
# 입력 : int
# 출력 : int

import math

def solution(n):
    return -1 if math.ceil(math.sqrt(n)) != math.floor(math.sqrt(n)) \
                else (int(math.sqrt(n))+1) ** 2