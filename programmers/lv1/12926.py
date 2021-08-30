# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/12926
# 시저 암호

def solution(s, n):
    lst = [ord(c) for c in s]
    l = []

    for i in lst:
        if not chr(i).isalpha():
            l.append(chr(i))
        elif (chr(i+n).islower() and chr(i).islower()) or \
            (chr(i+n).isupper() and chr(i).isupper()):
            l.append(chr(i+n))
        else:
            l.append(chr(i+n-26))
    
    return ''.join(l)