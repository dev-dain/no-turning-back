n = int(input())
s = ''
if n == 12 or n // 3 == 0:
    s = 'winter'
elif n // 3 == 1:
    s = 'spring'
elif n // 3 == 2:
    s = 'summer'
else:
    s = 'fall'
print(s)