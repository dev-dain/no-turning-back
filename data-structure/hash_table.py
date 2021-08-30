from linkedlistfifo import LinkedListFIFO
# key-value 연결, 한 키가 0 또는 1개의 값과 연관됨
# 키는 해시 함수를 계산할 수 있어야 하며
# 해시 테이블은 해시 버킷 배열로 구성됨
# 두 키가 동일한 버킷에 해시될 때 해시 충돌 문제 발생
# 버킷에 대해 키-값 쌍의 연결 리스트를 저장
# 해시 테이블의 조회, 삽입, 삭제 O(1)
class HashTable:
  def __init__(self, size):
    self.size = size
    self.slots = []
    self._createHashTable()

  def _createHashTable(self):
    for i in range(self.size):
      self.slots.append(LinkedListFIFO()) # 각 슬롯에 연결 리스트를 갖다 붙임
  
  def _find(self, item):
    return item % self.size # item의 슬롯 자리를 찾음

  def _add(self, item):
    index = self._find(item)
    self.slots[index].addNode(item)

  def _delete(self, item):
    index = self._find(item)
    self.slots[index].deleteNodeByValue(item)

  def _print(self):
    for i in range(self.size):
      print('슬롯(slot) {0}:'.format(i))
      self.slots[i].printList()

h1 = HashTable(3)
for i in range(0, 20):
  h1._add(i)
h1._print()
print('\n항목 0, 1, 2를 삭제')
h1._delete(0)
h1._delete(1)
h1._delete(2)
h1._print()