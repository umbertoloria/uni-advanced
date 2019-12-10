class LinkedList:
	class Node:
		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def add_head(self, element):
		new_node = self.Node(element, self._head)
		if self._size == 0:
			self._tail = new_node
		self._head = new_node
		self._size += 1

	def add_tail(self, element):
		new_node = self.Node(element, None)
		if self._size == 0:
			self._head = new_node
		else:
			self._tail._next = new_node
		self._tail = new_node
		self._size += 1

	def __len__(self):
		return self._size

	def __getitem__(self, j):
		cnt = 0
		# Consideriamo anche indici negativi alla Python
		if j < 0:
			j = self._size + j
		if j < 0 or j >= self._size:
			raise IndexError()
		current = self._head
		while current != None:
			if cnt == j:
				return current._element
			else:
				current = current._next
				cnt += 1

	def __str__(self):
		to_return = '<'
		current = self._head
		while current != None:
			to_return += str(current._element)
			current = current._next
			if current != None:
				to_return += ','
		to_return += '>'
		return to_return


lst = [1, 3, 5, 6]
lista = LinkedList()
for var in lst:
	lista.add_head(var)

print(lista)
if lista:
	print("lista piena")
else:
	print("lista vuota")

print(lista[1])
print(lista[-1])

if 5 in lista:
	print("presente")
else:
	print("assente")

for var in lista:
	print(var, end=' ')
