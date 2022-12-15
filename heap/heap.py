import heapq

class Median:
  def __init__(self):
    self.small= [] # maxheap
    self.large = [] # minheap

  def insert(self, num: int)->None:
    if len(self.large) == 0 or num < self.large[0]:
      heapq.heappush(self.small, -1 * num)
    else:
      heapq.heappush(self.large, num)

    if len(self.small) > len(self.large) + 1:
      val = -1 * heapq.heappop(self.small)
      heapq.heappush(self.large, val)
    elif len(self.small) + 1 < len(self.large):
      val = heapq.heappop(self.large)
      heapq.heappush(self.small, val)
  
  def getMedian(self):
    if len(self.small) == 0 and len(self.large) == 0:
      return None
    elif (len(self.small) + len(self.large)) % 2 == 0:
      return (-1 * self.small[0] + self.large[0]) / 2
    elif len(self.small) > len(self.large):
      return -1 * self.small[0]
    else:
      return self.large[0]

if __name__ == "__main__":
  median = Median()
  median.insert(7)
  median.insert(3)
  median.insert(4)
  median.insert(5)
  median.insert(2)
  print(median.small)
  print(median.large)
  print(median.getMedian())
  # 3 4 5 7
