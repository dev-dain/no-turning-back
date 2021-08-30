# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/81301
# 숫자 문자열과 영단어

def solution(s):
    if s.isdigit(): return int(s)
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(num)):
        if num[i] not in s: continue
        s = str(i).join(s.split(num[i]))
    return int(s)