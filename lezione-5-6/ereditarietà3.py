class Base:
	def __init__(self, v):
		self.a = v

	def f(self):
		print("base --", "a =", self.a)


class Der(Base):
	def f(self):
		print("der --", "a =", self.a)


class DerDer(Der):
	def f(self):
		print("derder --", "a =", self.a)


x = Der(10)
super(Der, x).f()

print()
y = DerDer(20)
super(DerDer, y).f()
super(Der, y).f()
