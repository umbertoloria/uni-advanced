class A:
	def ciao(self):
		print("cia da A")


class B:
	def ciao(self):
		print("cia da B")


class C:
	def ciao(self):
		print("cia da C")


class D(A, B, C):
	pass


d = D()
print(D.__bases__)
d.ciao()
D.__bases__ = (C, A, B)
print(D.__bases__)
d.ciao()
