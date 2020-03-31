# Python implementation of Doubly linked list 
import sys

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0


	# Empty the linked list, O(1)
	def clear(self):
		self.head = self.tail = None
		self.size = 0

	# Return the size of the linked list, O(1)
	def size(self):
		return self.size

	# Return if the linked list is empty, O(1)
	def is_empty(self):
		return self.size()==0

	# Insert a node at the front of the list, O(1)
	def insert_at_front(self, data):
		node = Node(data)
		if self.head is None:
			self.head = self.tail = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node
		self.size += 1

	# Insert a node at the end of the list, O(1)
	def insert_at_end(self, data):
		node = Node(data)
		if self.head is None:
			self.head = self.tail = node
		else:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node
		self.size += 1

	# Insert an element at the given index in the linked list, O(n)
	def insert_at(self, index, data):
		assert 0 <= index < self.size, "Index out of range"
		node = Node(data)
		curr = self.head
		curr_index = 0
		while curr_index != index-1:
			curr = curr.next
			curr_index += 1

		node.next = curr.next
		curr.next.prev = node
		curr.next = node
		node.prev = curr
		self.size += 1

	# Remove the node at the front of the linked list, O(1)
	def pop_front_node(self):
		assert self.head is not None, "List is empty"
		if self.head == self.tail:
			head = self.head
			self.head = self.tail = None
		else:
			head, self.head = self.head, self.head.next
			self.head.prev = None
		self.size -= 1
		return head.data

	#Remove the node at the end of the linked list, O(1)
	def pop_tail_node(self):
		assert self.head is not None, "List is empty"
		if self.head == self.tail:
			tail = self.tail
			self.head = self.tail = None
		else:
			tail, self.tail = self.tail, self.tail.prev
			self.tail.next = None
		self.size -= 1
		return tail.data