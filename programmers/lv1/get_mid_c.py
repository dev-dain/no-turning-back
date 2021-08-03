# https://programmers.co.kr/learn/courses/30/lessons/12903
# 가운데 글자 가져오기
# 입력 : str
# 출력 : str

import math
def solution(s):
    return s[math.ceil(len(s)/2-1):math.floor(len(s)/2+1)]