# Python implementation of Singly linked list 

Class Node():
	def __init__(self, value):
		self.value = value
		self.next = None


Class SinglyLinkedList():
	def __init__(self):
		self.head = None


	# Insert a node at the front of the list
	def insert_at_front(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node


	# Insert a node at the end of the list
	def insert_at_end(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
		else:
			tail = self. head
			while tail.next is not None:
				tail = tail.next
			tail.next = node


	# Insert a node after the given node in the list






