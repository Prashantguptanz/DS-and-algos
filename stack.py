# Python implementation of Stack data structure

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.top = None

	# Push an item to the stack, O(1)
	def push(self, data):
		node = Node(data)

		if self.top is None:
			self.top = node
		else:
			node.next = self.top
			self.top = node

	# Pop and item from the stack, O(1)
	def pop(self):
		assert self.top is not None, "Empty Stack"
		data = self.top.data
		self.top = self.top.next
		return data

	# Peek an item from the top of the stack, O(1)
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