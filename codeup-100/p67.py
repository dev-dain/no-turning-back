n = int(input())
if n < 0:
    print("A") if n % 2 == 0 else print("B")
else:
    print("C") if n % 2 == 0 else print("D")