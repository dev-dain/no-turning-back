# bisect 모듈로 이진 검색 가능
from bisect import bisect

l = [0, 3, 4, 8, 10]
print(bisect(l, 4))
print(bisect(l, -1))  # 예외. 0