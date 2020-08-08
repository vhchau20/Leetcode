class Node:
	def __init__(self):
		self.children = {} # char to Node
		self.end = False

class WordDictionary:
	def __init__(self):
		self.root = Node()

	def addWord(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				node.children[char] = Node()
			node = node.children[char]
		node.end = True

	def search(self, word):
		return self.helper(self.root, word)

	def helper(self, node, word):
		for i in range(len(word)):
			c = word[i]
			if c == ".":
				for j in node.children:
					if self.helper(node.children[j], word[i+1:]):
						return True
				return False
			elif c not in node.children:
				return False
			node = node.children[c]
		return node.end



dic = WordDictionary()
dic.addWord("to")
dic.addWord("tea")
dic.addWord("ted")
dic.addWord("ten")
dic.addWord("inn")

# print dic.search("to")
print dic.search("...")