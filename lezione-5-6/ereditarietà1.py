class Base:
	def __init__(self, a, b):
		self._a = a
		self._b = b

	def stampa(self):
		print("<{0}>,<{1}>".format(self._a, self._b))


class Derivata(Base):
	def __init__(self, a, b, c):
		super().__init__(a, b)
		self._c = c

	def stampa(self):
		print("[{0}]-[{1}]".format(self._a, self._b))


b = Base(1, 3)
b.stampa()
d = Derivata('a', 'b', 9)
d.stampa()
