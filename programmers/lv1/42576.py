# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    athletes = Counter(participant)
    for a in completion:
        athletes[a] -= 1
    return athletes.most_common(1)[0][0]

# Counter끼리 뺄셈 연산이 가능하기 때문에 그냥 빼버려도 상관없음
# Counter(participant) - Counter(completion)