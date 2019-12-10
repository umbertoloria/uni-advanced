print("******Provo slots*******")


class MyClass:
	__slots__ = ("nome", "cognome", "eta")

	def __init__(self, nome, cognome, eta):
		self.nome = nome
		self.cognome = cognome
		self.eta = eta


m = MyClass("a", "b", "c")
print(m)

print()
print()

print("******Provo Singleton*******")


class MySingleton:
	sharedState = {}

	def __new__(cls, *args, **kwargs):
		x = super(MySingleton, cls).__new__(cls, *args, **kwargs)
		x.__dict__ = MySingleton.sharedState
		return x


i1 = MySingleton()
i1.x = 5
print(i1.x)

i2 = MySingleton()
print(i2.x)

i2.y = 45
print(i1.y)
