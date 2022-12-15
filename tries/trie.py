
class TrieNode:
  def __init__(self):
    self.children = {}
    self.word = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  # time: O(1)
  def insert(self, word):
    cur = self.root

    for ch in word:
      if ch not in cur.children:
        cur.children[ch] = TrieNode()
      cur = cur.children[ch]
    cur.word = True
  
  # time: O(1)
  def contains(self, word):
    cur = self.root
    
    for ch in word:
      if ch not in cur.children:
        return False
      else:
        cur = cur.children[ch]
    return cur.word

  # time: O(1)
  def containsPrefix(self, prefix):
    cur = self.root
    for ch in prefix:
      if ch not in cur.children:
        return False
      else:
        cur = cur.children[ch]
    return True




if __name__ == "__main__":
  trie = Trie()
  trie.insert("same")
  trie.insert("sachin")
  if trie.containsPrefix("sach"):
    print("word is present")

  
