# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어

def solution(arr):
    last = arr[0]
    lst = [last]
    for i in range(len(arr)):
        if i == 0: continue
        if arr[i] == last:
            continue
        lst.append(arr[i])
        last = arr[i]
    return lst
