class Stack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, item):
		self.stack.append(item)
		return "item is added to the stack"
	
	def pop(self):
		if self.is_empty():
			return "stack is empty"
		return self.stack.pop()

	def __str__(self):
		return str(self.stack)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print("my_stack: ",my_stack)
print("pop stack",my_stack.pop())
print("stack after pop", my_stack)

