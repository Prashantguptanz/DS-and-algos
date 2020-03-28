# Python implementation of Binary Heap

class BinaryHeap:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	# Insert an element in the heap, O(log n)
	def insert(self, k):
		self.heap.append(k)
		self.size += 1
		self.percup(self.size)

	# Heapify the heap, O(log n)
	def percup(self, i):
		while i//2 >0:
			parent_index = i//2
			child_index = i
			if self.heap[parent_index] < self.head[child_index]:
				break
			else:
				heap[child_index], heap[parent_index] = heap[parent_index], heap[child_index]
				i = i//2

	# Heapify the heap, O(log n)
	def percdown(self, i):
		while 2*i <= self.size:
			parent_index = i
			min_child_index = self.min_child(i)
			if self.heap[parent_index] < self.heap[min_child_index]:
				break
			if self.heap[parent_index] > self.heap[min_child_index]:
				self.heap[parent_index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[parent_index]
			i = min_child_index

	# return the min child of a node, O(1)
	def min_child(self, i):
		if self.size < 2*i + 1:
			return 2*i
		else:
			if self.heap[2*i] > self.heap[2*i + 1]:
				return 2*i + 1
			else:
				return 2*i

	# Delete the min element (root) of the heap, O(log n)
	def del_min(self):
		return_val = self.heap[1]
		self.heap[1] = self.heap[self.size]
		self.heap.pop()
		self.size -= 1
		self.percdown(1)
		return return_val

	# Build a heap from a given list, O(n) (check this http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf)
	def buildHeap(self, alist):
		i = len(alist) // 2
		self.size = len(alist)
		self.heap = [0] + alist[:]
		while (i > 0):
			self.percdown(i)
			i = i - 1


if __name__ == "__main__":
	my_heap = BinaryHeap()
	my_heap.buildHeap([5, 7, 12, 15, 8, 7, 6, 9, 10])
	print (my_heap.heap)
	my_heap.del_min()
	print (my_heap.heap)