# 최대힙 구현
class Heapify:
  def __init__(self, data=None):
    self.data = data or []
    for i in range(len(data)//2, -1, -1):
      self.__max_heapify__(i)

  def __repr__(self):
    return repr(self.data)

  def parent(self, i):
    # if i & 1: # 홀수번째(오른쪽 자식)이라면
    return i >> 1
    # else: # 짝수번째(왼쪽 자식)이라면
    #   return (i >> 1) - 1 # 흠?

  def left_child(self, i):
    return (i << 1) + 1

  def right_child(self, i):
    return (i << 1) + 2

  def __max_heapify__(self, i):
    largest = i # 현재 노드
    left = self.left_child(i)
    right = self.right_child(i)
    n = len(self.data)

    # 왼쪽 자식의 값이 더 크면 왼쪽 자식 인덱스를, 그렇지 않으면 현재 부모인 i로 largest를 정함
    largest = (left < n and self.data[left] > self.data[i]) and left or i
    # 오른쪽 자식 값이 더 크면 오른쪽 자식 인덱스를, 그렇지 않으면 현재 largest로 정함
    largest = (right < n and self.data[right] > self.data[largest]) and right or largest

    # 현재 노드가 자식보다 작다면 swap
    if i is not largest:
      self.data[i], self.data[largest] = self.data[largest], self.data[i]
      self.__max_heapify__(largest)

  def extract_max(self):
    n = len(self.data)
    max = self.data[0]  # 일단 큰 값을 빼주고
    self.data[0] = self.data[-1]  # 가장 아래 것을 루트로 올림
    self.data = self.data[:n-1] # 1개 줄이기
    self.__max_heapify__(0) # 0부터 다시 max_heapify
    return max

  def insert(self, item):
    i = len(self.data)
    self.data.append(item)
    while i != 0 and item > self.data[self.parent(i)]:  # item이 현재 밑바닥 부모 인덱스 값보다 크다면...
      self.data[i] = self.data[self.parent(i)]  # i번 인덱스 값을 부모 것으로 바꿈
      i = self.parent(i)  # i 인덱스도 부모 인덱스로 바꿔버림
    self.data[i] = item # 제자리를 찾았으므로 해당 인덱스에 item을 넣어줌

l1 = [3, 2, 5, 1, 7, 8, 2]
h = Heapify(l1)
print(h.extract_max() == 8)