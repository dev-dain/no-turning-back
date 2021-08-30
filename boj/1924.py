# 08-18
# 입출력
from datetime import date
day = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')

x, y = map(int, input().split())
print(day[date(2007, x, y).weekday()])