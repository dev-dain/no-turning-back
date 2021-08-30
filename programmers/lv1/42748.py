# 08-03
# https://programmers.co.kr/learn/courses/30/lessons/42748
# K번째 수 구하기
# 입력 : List[int], List[int]
# 출력 : List[int]

def solution(array, commands):
    answer = []
    for command in commands:
        lst = sorted(array[command[0]-1:command[1]])
        answer.append(lst[command[2]-1])
    return answer