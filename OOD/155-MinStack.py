# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.s = []

	def push(self, x):
		"""
		:type x: int
		:rtype: None
		"""
		if not self.s:
			self.s.append( (x,x) )
			return
		
		if x > self.getMin():
			self.s.append( (x,self.getMin()) )
		else:
			self.s.append( (x,x) )
			
		

	def pop(self):
		"""
		:rtype: None
		"""
		return self.s.pop()[0]

	def top(self):
		"""
		:rtype: int
		"""
		return self.s[-1][0]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
x = [5,10,7,3]
for i in x:
	obj.push(i)
print obj.s
print obj.pop()
print obj.top()
print obj.getMin()
print obj.s