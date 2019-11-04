class Base:
	def f(self):
		print("Base")


class Der(Base):
	def f(self):
		print("Der")

	def g(self):
		self.f()
		super().f()
		super(Der, self).f()
		Base.f(self)


class DerDer(Der):
	def f(self):
		print("DerDer")

	def h(self):
		self.f()
		super().f()
		super(DerDer, self).f()
		super(Der, self).f()


x = Der()
x.g()

print()
y = DerDer()
y.h()
