class Node:
	def __init__(self):
		self.children = {} # char to node
		self.isEnd = False

class WordDictionary:

	def __init__(self):
		self.root = Node()

	def addWord(self, word):
		node = self.root
		for char in word:
			if char in node.children:
				node.children[char] = Node()
			node = node.children[char]
		node.isEnd = True

	def search(self, word):
		return self.root

dic = WordDictionary()
dic.addWord("hello")

