class dfs:
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  

  # time and space: O(n)
  def inOrder(self):
    stack = []
    curr = self

    while curr or stack:
      if curr:
        stack.append(curr)
        curr = curr.left
      else:
        curr = stack.pop()
        print(curr.val, end=" ")
        curr = curr.right
  

  # time and space: O(n)
  def preOrder(self):
    stack = []
    curr = self
    
    while curr or stack:
      if curr:
        print(curr.val, end=" ")
        stack.append(curr.right)
        curr = curr.left
      else:
        curr = stack.pop()
  

  # time and space: O(n)
  def postOrder(self):
    stack = [self]
    visit = [False]
    curr = self

    while stack:
      curr, visited = stack.pop(), visit.pop()
      if curr:
        if visited: # all children visited
          print(curr.val, end=" ")
        else:
          stack.append(curr)
          visit.append(True)
          stack.append(curr.right)
          visit.append(False)
          stack.append(curr.left)
          visit.append(False)


#            1
#          /   \
#         2     3
#        / \   / \
#       4   5 6   7

if __name__ == "__main__":
  left_tree = dfs(2, dfs(4), dfs(5))
  right_tree = dfs(3, dfs(6), dfs(7))
  a = dfs(1, left_tree, right_tree)
  a.postOrder()
  print()