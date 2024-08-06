class Queue(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		if len(self.queue) < 1:
			return None
		return self.queue.pop(0)

	def display(self):
		return self.queue

	def size(self):
		return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(f"queue data: {queue.display()}")
print(queue.dequeue())
print(f"Queue data after dequeue {queue.display()}")
		