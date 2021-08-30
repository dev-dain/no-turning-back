# 퀵 정렬
# 입력 : 리스트 l, 범위 start, end
# 출력 : void

def solution(l, start, end):
    # 정렬 대상이 1개 이하이면 종료
    if end - start <= 0: return

    print(start, end)

    pivot = l[end] # 기준값을 정함. 편의상 마지막 값을 피봇값으로
    i = start
    for j in range(start, end):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[end] = l[end], l[i]

    # 재귀 호출
    solution(l, start, i - 1)   # 기준 값보다 작은 그룹을 재귀 호출로 정렬
    solution(l, i + 1, end) # 기준 값보다 큰 그룹을 재귀 호출로 정렬


def quick_sort(l):
    solution(l, 0, len(l)-1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)