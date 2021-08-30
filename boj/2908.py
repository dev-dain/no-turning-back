# 08-19
lst = input().split()
lst = [int(s[::-1]) for s in lst]
print(max(lst))