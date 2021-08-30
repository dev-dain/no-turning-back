# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/77884
# 약수의 개수와 덧셈

def solution(left, right):
    l = []
    for i in range(left, right+1):
        cnt = [j for j in range(i//2,0,-1) if i % j == 0]
        l.append(i) if len(cnt) % 2 else l.append(-i)
    return sum(l)


'''
참고할만함.
제곱수는 약수의 개수가 홀수이다
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

'''