# 08-03
# https://programmers.co.kr/learn/courses/30/lessons/82612
# 입력 : int, int, int
# 출력 : int

def solution(price, money, count):
    n_enough = money - ((price+price*count) * count / 2)
    return 0 if n_enough > 0 else abs(n_enough)