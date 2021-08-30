# 힙을 사용해 우선순위 큐 구현
# 힙은 각 노드가 하위 노드보다 작은(또는 큰) 이진트리
# 리스트에서 가장 작거나 큰 요소에 반복적으로 접근하는 프로그램에 적합
# 조회, 추가, 삭제 시간복잡도 O(log n)
# 힙은 이진 트리지만 bst는 아니기 때문에 반드시 왼쪽 자식이 더 작지는 않음
import heapq

lst1 = [2, 6, 3, 8, 1]
heapq.heapify(lst1) # lst1을 힙으로 변환함 O(n)
print(lst1) # 다만 정렬이 아니기에 0이 맨 위에 가는 것만 보장
heapq.heappush(lst1, 5)
heapq.heappush(lst1, 0)
print(lst1)
heapq.heappop(lst1)
print(lst1)

heapq.heappushpop(lst1, 4)  # 추가 후 삭제
heapq.heapreplace(lst1, 9)  # 삭제 후 추가
print(lst1)

print(heapq.nlargest(3, lst1))  # 3개의 가장 큰 요소가 든 리스트 반환
print(heapq.nsmallest(3, lst1)) # 3개의 가장 작은 요소가 든 리스트 반환

# heapq.merge를 사용하면 여러 이터러블을 병합해 정렬된 이터레이터 반환
for x in heapq.merge([1, 3, 5], [2, 4, 6]):
  print(x, end=' ')
