# 10-23
import math

def solution(arr):
    g = 1
    while len(arr) > 1:
        x, y = arr.pop(), arr.pop()
        arr.append(x * y // math.gcd(x, y))
    return arr[0]