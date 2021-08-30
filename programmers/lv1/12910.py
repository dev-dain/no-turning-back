# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/12910
# 나눠 떨어지는 숫자 배열

def solution(arr, divisor):
    res_arr = sorted(list(filter(lambda x : x % divisor == 0, arr)))
    return [-1] if len(res_arr) == 0 else res_arr