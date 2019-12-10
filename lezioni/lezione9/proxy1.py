class Implementation:

	def f(self):
		print("f")

	def g(self):
		print("g")

	def h(self):
		print("h")


class Proxy:

	def __init__(self):
		self.__impl = Implementation()

	def f(self):
		self.__impl.f()

	def g(self):
		self.__impl.g()

	def h(self):
		self.__impl.h()


p = Proxy()
p.f()
p.g()
p.h()
