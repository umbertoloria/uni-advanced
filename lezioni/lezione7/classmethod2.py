class Spam:
	instances_count = 0

	def __init__(self):
		self.count()

	@classmethod
	def count(cls):
		cls.instances_count += 1

	@classmethod
	def print_instances_count(cls):
		print(cls.instances_count)


class Sub(Spam):
	instances_count = 0

	def __init__(self):
		Spam.__init__(self)


class Other(Spam):
	instances_count = 0


a = Spam()
m, n = Sub(), Sub()
x, y, z = Other(), Other(), Other()

Spam.print_instances_count()
a.print_instances_count()
print()
Sub.print_instances_count()
m.print_instances_count()
print()
Other.print_instances_count()
x.print_instances_count()
