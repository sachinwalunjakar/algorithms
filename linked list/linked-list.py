class LinkedNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
# 1 2 3 4 5
class LinkedList:
  def middleOfList(self, head):
    slow, fast = head, head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    print(slow.val)
    return slow



if __name__ == "__main__":
  ll = LinkedNode(0, LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4)))))
  LinkedList().middleOfList(ll)
  
