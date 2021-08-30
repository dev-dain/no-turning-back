# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 비밀지도

def solution(n, arr1, arr2):
    combi = [bin(a1 | a2)[2:].rjust(n, '0') for a1, a2 in zip(arr1, arr2)]
    return [''.join('#' if int(b) & 1 else ' ' for b in row) for row in combi]