# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기

def solution(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])