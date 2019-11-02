# Definire un decoratore di classe che permette alla classe decorata di contare le sue istanze.

def decoratore(classe):
	classe.instances_count = 0

	old_constructor = classe.__init__

	def new_constructor(self):
		classe.instances_count += 1
		old_constructor(self)

	classe.__init__ = new_constructor

	def get_instances_count():
		return classe.instances_count

	classe.getInstancesCount = get_instances_count
	return classe


@decoratore
class ClasseBella:

	def __init__(self):
		self.x = 1

	def __str__(self):
		return str(self.x)


a = ClasseBella()
b = ClasseBella()
c = ClasseBella()
print(a)
print(b)
print(c)
print(ClasseBella.getInstancesCount())
