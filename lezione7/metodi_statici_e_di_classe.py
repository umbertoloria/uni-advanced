class Spam:
	instances_count = 0

	def __init__(self):
		Spam.instances_count += 1

	@staticmethod
	def print_instances_count():
		print(Spam.instances_count)


class Cpam:
	instances_count = 0

	def __init__(self):
		Cpam.instances_count += 1

	@classmethod
	def print_instances_count(cls):
		print(cls.instances_count)


z = Cpam()
for i in range(2):
	Cpam()
Cpam.print_instances_count()
z.print_instances_count()
