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

	def __getattr__(self, name):
		return getattr(self.__impl, name)


p = Proxy()
p.f()
p.g()
p.h()
