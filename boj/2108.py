# 08-26
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
# 이렇게 하면 전체 빈도 수를 볼 수 있음
'''
5
-3
-3
-2
1
0
'''
most_freq_cnt = Counter(arr).most_common(1)[0][1]
most_freq_el = [e[0] for e in Counter(arr).most_common() if e[1] == most_freq_cnt]

# round(float)
print(round(sum(arr) / len(arr)))
print(arr[len(arr)//2])
print(most_freq_el[0] if len(most_freq_el) == 1 else most_freq_el[1])
print(max(arr) - min(arr))
