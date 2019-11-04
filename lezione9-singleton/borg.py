class Borg:
	__shared_state = {}

	def __new__(cls, *args, **kwargs):
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls.__shared_state
		return obj


class Child(Borg):
	pass


borg1 = Borg()
borg2 = Borg()
print(borg1 is borg2)
borg1.only_one_var = "I'm the only one"
print(borg1.only_one_var)

child = Child()
print(child.only_one_var)
