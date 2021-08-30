# 이진수에서 모든 1의 위치 찾기
# 입력 : int, int...
# 출력 : int

n = int(input())
b_list = [bin(int(input()))[2:] for _ in range(n)]
idx_list = [list(reversed([len(b)-i-1 for i in range(len(b)) if b[i] == '1'])) 
            for b in b_list]
for idx in idx_list:
  for i in idx:
    print(i, end=' ')
  print()

# 오호 이것도 된다
# for _ in range(int(input())) 해서 즉석으로 range에 넣을 값을 받을 수 있음
