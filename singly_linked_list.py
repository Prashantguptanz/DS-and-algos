# Python implementation of Singly linked list 
import sys

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class SinglyLinkedList:
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
	def insert_after(self, key_node, value):
		node = Node(value)
		trav = self.head
		while trav is not None and trav is not key_node:
			trav = trav.next

		if trav is None:
			Print("The key node is not found")
		elif trav.next is None:
			trav.next = node
		else:
			next_node = trav.next
			trav.next = node
			node.next = next_node


	# Remove the node at the front of the linked list
	def pop_front_node(self):
		if self.head is None:
			print ("List is empty")
			return

		head = self.head
		self.head = head.next
		head.value = None
		head.next = None

	#Remove the node at the end of the linked list
	def pop_tail_node(self):
		curr = self.head
		if curr is None:
			Print ("Empty list")
			return

		prev = None

		while curr.next is not None:
			prev = curr
			curr = curr.next

		if prev == None:
			self.head = None
			curr.value = None
		else:
			prev.next = None
			curr.value = None

	# Remove the given node from the linked list
	def remove(self, node):
		curr = self.head
		if curr is None:
			print ("Empty list")
			return

		prev = None

		while curr is not None and curr is not node:
			prev = curr
			curr = curr.next

		if curr is None:
			print ("Node not found")
		elif prev is None:
			self.head = self.head.next
			curr = None
		else:
			prev.next = curr.next
			curr = None


	#Check if a node is in the list
	def check_node(self, node):
		if self.head is None:
			Print ("Empty list")
			return

		curr = self.head

		while curr is not None and curr is not node:
			curr = curr.next

		if curr is None:
			return False

		return True

	# print all the items
	def printlist(self):
		if self.head is None:
			print ("Nothing to display")
		else:
			curr = self.head
			while curr != None:
				sys.stdout.write(str(curr.value) + ' ')
				curr = curr.next
			print('\n')


if __name__ == '__main__':
    list = SinglyLinkedList()
    list.insert_at_front(4)
    list.insert_at_front(3)
    list.insert_at_front(2)
    list.insert_at_end(10)
    list.insert_after(list.head, 7)
    list.remove(list.head.next)
    print(list.check_node(list.head.next))
    list.printlist()


















