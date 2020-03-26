# Python implementation of Stack data structure

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.top = None

	def push(self, data):
		node = Node(data)

		if self.top is None:
			self.top = node
		else:
			node.next = self.top
			self.top = node

	def pop(self):
		assert self.top is not None, "Empty Stack"
		data = self.top.data
		self.top = self.top.next
		return data

	def peek(self):
		assert self.top is not None, "Empty Stack"
		return self.top.data

if __name__ == '__main__':
    stack = Stack()
    stack.push(40)
    stack.push(30)
    stack.push(22)
    print (stack.peek())
    print (stack.pop())
    print (stack.pop())
    print (stack.peek())