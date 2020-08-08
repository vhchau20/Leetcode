# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class node:
	def __init__(self):
		self.children = {}
		self.end = False

class Trie:
	def __init__(self):
		self.root = node()

	def insert(self, word):
		curr = self.root
		for char in word:
			if char not in curr.children:
				curr.children[char] = node()
			curr = curr.children[char]
		curr.end = True

	def search(self, word):
		curr = self.root
		for char in word:
			if char in curr.children:
				curr = curr.children[char]
			else:
				return False
		return curr.end

	def startsWith(self, prefix):
		curr = self.root
		for char in prefix:
			if char in curr.children:
				curr = curr.children[char]
			else:
				return False
		return True


trie = Trie();

print trie.insert("apple")
print trie.search("apple")
print trie.search("app")
print trie.startsWith("app")
print trie.insert("app")