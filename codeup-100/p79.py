n = int(input())
i = 1
sum = 0
while True:
    sum += i
    if sum >= n:
        print(i)
        break
    i += 1