# https://programmers.co.kr/learn/courses/30/lessons/12948
# 핸드폰 번호 가리기

def solution(phone_number):
    return phone_number[-4:].rjust(len(phone_number), '*')