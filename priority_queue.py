# Python implementation of Priority Queue using binary heap
from binary_heap import BinaryHeap


class PriorityQueue:
	def __init__(self):
		self.pq = BinaryHeap()

	def enqueue(self, k):
		self.pq.insert(k)

	def dequeue(self):
		return self.pq.del_min()

	def peek(self):
		return self.pq.heap[1]


if __name__ == "__main__":
	mypq = PriorityQueue()
	mypq.enqueue(5)
	mypq.enqueue(2)
	mypq.enqueue(7)
	print(mypq.peek())
	print(mypq.dequeue())
	print(mypq.dequeue())

