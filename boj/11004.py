# 08-19
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = sorted(map(int, input().split()))
print(lst[k-1])