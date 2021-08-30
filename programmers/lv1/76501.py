# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/76501
# 음양 더하기

def solution(absolutes, signs):
    return sum([num if sign else -num for num, sign in zip(absolutes, signs)])
