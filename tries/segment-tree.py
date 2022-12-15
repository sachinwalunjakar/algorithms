class SegmentTree:
  def __init__(self, total, l, r):
    self.sum = total
    self.left = None
    self.right = None
    self.l = l
    self.r = r

  # time: O(n)
  @staticmethod
  def build(num, l, r):
    if l == r:
      return SegmentTree(num[l], l, r)

    M = (l + r) // 2
    root = SegmentTree(0, l, r)
    root.left = SegmentTree.build(num, l, M)
    root.right = SegmentTree.build(num, M+1, r)
    root.sum = root.left.sum + root.right.sum

    return root

  # time: O(logn)
  def queryRange(self, l, r):
    if(self.l == l and self.r == r):
      return self.sum

    M = (self.l + self.r) // 2
    if r <= M:
      return self.left.queryRange(l, r)
    elif l > M:
      return self.right.queryRange(l, r)
    else: # overlapping range
      M = (l + r) // 2
      return self.queryRange(l, M) + self.queryRange(M+1, r)


  def update(self, index, val):
    if self.l == self.r:
      self.sum = val
      return

    M = (self.l + self.r) // 2
    if index <= M:
      self.left.update(index, val)
    else:
      self.right.update(index, val)
    
    self.sum = self.left.sum + self.right.sum



if __name__ == "__main__":
  nums = [0,1,2,3,4,5,6]
  segmentTree = SegmentTree.build(nums, 0, 6)
  segmentTree.update(3, 100)