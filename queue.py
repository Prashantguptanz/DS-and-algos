# Python implementation of Queue data structure

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	# Add an item to the queue, O(1)
	def enqueue(self, data):
		node = Node(data)
		if self.tail == None:
			self.head = self.tail = node

		node.next = self.tail
		self.tail.prev = node
		self.tail = node

	# Remove an item from the queue, O(1)
	def dequeue(self):
		assert self.head is not None, "Empty queue"
		data = self.head.data

		if self.head == self.tail:
			self.head = self.tail = None
			return data
		else:
			self.head = self.head.prev
			self.head.next = None
			return data

	# Peek the front item of the queue, O(1)
	def peek(self):
		assert self.head is not None, "Empty queue"
		return self.head.data

if __name__ == "__main__":
	queue = Queue()
	queue.enqueue(34)
	queue.enqueue(35)
	queue.enqueue(41)
	queue.enqueue(56)
	print (queue.dequeue())
	print (queue.dequeue())
	print (queue.dequeue())
	queue.enqueue(70) 
	print (queue.peek())



