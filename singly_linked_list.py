# Python implementation of Singly linked list 
import sys

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	# Empty the linked list, O(1)
	def clear(self):
		self.head = None
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
		if not self.head is None:
			node.next = self.head
		self.head = node
		self.size += 1

	# Insert a node at the end of the list, O(n)
	def insert_at_end(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			curr = self.head
			while not curr.next is None:
				curr = curr.next
			curr.next = node
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
		curr.next = node
		self.size += 1

	# Remove the node at the front of the linked list, O(1)
	def pop_front_node(self):
		assert self.head is not None, "List is empty"
		head, self.head = self.head, self.head.next
		data = head.data
		head = None
		self.size -= 1
		return data

	#Remove the node at the end of the linked list, O(n)
	def pop_tail_node(self):
		assert self.head is not None, "List is empty"
		prev, curr = None, self.head

		while not curr.next is None:
			prev = curr
			curr = curr.next

		if curr is self.head:
			self.head = curr = None
		else:
			prev.next = curr = None
		self.size -= 1

	# Remove the given node from the linked list, O(n)
	def remove(self, node):
		assert self.head is not None, "List is empty"
		prev, curr = None, self.head

		while curr is not None and curr is not node:
			prev = curr
			curr = curr.next

		assert curr is not None, "Node not found"
		if prev is None:
			self.head = curr.next
		else:
			prev.next = curr.next
		curr = None
		self.size -= 1

	# Remove the node at the given index, O(n)
	def remove_at_index(self, index):
		assert self.head is not None, "List is empty"
		assert 0 <= index < self.size, "Index out of range"
		prev, curr = None, self.head
		curr_index = 0

		while curr_index != index:
			prev = curr
			curr = curr.next

		if prev is None:
			self.head = curr.next
		else:
			prev.next = curr.next
		curr = None
		self.size -= 1

	#Check if a node is in the list, O(n)
	def check_node(self, node):
		assert self.head is not None, "List is empty"
		curr = self.head

		while curr is not None and curr is not node:
			curr = curr.next

		if curr is None:
			return False
		return True

	# print all the items, O(n)
	def printlist(self):
		assert self.head is not None, "List is empty"
		curr = self.head
		while curr != None:
			sys.stdout.write(str(curr.data) + ' ')
			curr = curr.next
		print('\n')


if __name__ == '__main__':
    list = SinglyLinkedList()
    list.insert_at_front(4)
    list.insert_at_front(3)
    list.insert_at_front(2)
    list.insert_at_end(10)
    list.insert_at(2, 7)
    list.pop_front_node()
    list.remove(list.head.next)
    print(list.check_node(list.head.next))
    list.printlist()