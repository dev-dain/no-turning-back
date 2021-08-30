# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기

def solution(numbers):
    n_set = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n_set.add(numbers[i]+numbers[j])
    return list(sorted(n_set))