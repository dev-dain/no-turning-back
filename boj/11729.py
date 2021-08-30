# 08-21
def hanoi(n, start, dest, aux):
  if n == 1:
    print(start, dest)
    return
  
  hanoi(n-1, start, aux, dest)
  print(start, dest)
  hanoi(n-1, aux, dest, start)

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3, 2)