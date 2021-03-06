class Borg:
	__shared_state = {}

	def __new__(cls, *args, **kwargs):
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		# obj.__dict__ = cls.__shared_state
		try:
			obj.__dict__ = cls.__dict__["_{}__shared_state".format(cls.__name__)]
		except:
			obj.__dict__ = cls.__shared_state
		return obj


class Child(Borg):
	pass


class AnotherChild(Borg):
	__shared_state = {}


borg1 = Borg()
borg2 = Borg()
print(borg1 is borg2)
borg1.only_one_var = "I'm the only one"
print(borg1.only_one_var)

child1 = Child()
print(child1.only_one_var)

child2 = AnotherChild()
child2.x = 5
print(child2.x)
print(borg2.only_one_var)
