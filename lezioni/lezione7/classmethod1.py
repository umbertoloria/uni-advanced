class Spam:
	instances_count = 0

	def __init__(self):
		Spam.instances_count += 1

	@classmethod
	def print_instances_count(cls):
		print(cls.instances_count)


class Sub(Spam):
	pass


x = Spam()
y = Sub()
z = Sub()
z.print_instances_count()
