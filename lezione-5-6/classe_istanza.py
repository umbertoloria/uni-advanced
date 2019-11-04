class MyClass:
	# variabile di classe
	a = 3

	def method(self):
		# self.a inizialmente si riferisce a MyClass.a perché è la più vicina
		print("Class.a", id(MyClass.a))
		print("self.a", id(self.a))
		self.a = 4
		# self.a adesso è una variabile di istanza e si riferisce ad essa (è più vicina)
		# MyClass.a esiste ancora, ha solo una visibilità nascosta
		print("Class.a", id(MyClass.a))
		print("self.a", id(self.a))
		del self.a
		# self.a adesso si riferisce alla più vicina, che è MyClass.a, essendo al variabile di istanza inesistente
		print("Class.a", id(MyClass.a))
		print("self.a", id(self.a))


x = MyClass()
x.method()
