# 배열

class Array:
  def __init__(self):
    self.lst = []
    self.idx = 0

  def insertData(self, n):
    self.lst.append(n)
    self.idx += 1
  
  def insert(self, idx, n):
    self.lst.insert(idx, n)
    self.idx += 1

  def removeData(self):
    if self.idx == 0: return -1
    self.idx -= 1
    return self.lst.pop()

  def remove(self, idx):
    if self.idx == 0: return -1
    self.idx -= 1
    return self.lst.pop(idx)

  def traverse(self):
    for e in self.lst:
      print(e, end=' ')
    print()
  
  def search(self, x):
    try:
      return self.lst.index(x)
    except:
      return -1

  def __str__(self):
    return str(self.lst)


arr = Array()
print(arr)
arr.insertData(5)
arr.insertData(15)
arr.insertData(23)
print(arr)
arr.removeData()
arr.insert(1, 3)
arr.traverse()
print(arr.search(5))
print(arr.search(14))
