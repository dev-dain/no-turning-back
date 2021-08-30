# 08-20
y = int(input())
print(1) if y % 4 == 0 and (y % 100 or y % 400 == 0) else print(0) 