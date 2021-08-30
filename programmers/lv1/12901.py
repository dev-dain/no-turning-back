# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
# 2016년

import time
def solution(a, b):
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    date = '2016-%d-%d'%(a,b)
    t = time.strptime(date, '%Y-%m-%d')
    return day[t.tm_wday]

    # day[datetime.datetime(2016, a, b).weekday()]
