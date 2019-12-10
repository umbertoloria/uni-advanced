class Computer:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "the {} computer".format(self.name)

	def execute(self):
		return "executes a program"


class Synthesizer:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "the {} synthesizer".format(self.name)

	def play(self):
		return "is playing an electronic song"


class Human:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "{} the human".format(self.name)

	def speak(self):
		return "says hello"


class Adapter(Computer):

	def __init__(self, wih):
		self.wih = wih

	def execute(self):
		if isinstance(self.wih, Synthesizer):
			return self.wih.play()
		if isinstance(self.wih, Human):
			return self.wih.speak()


class WhatIUse:
	def op(self, wiw):
		return wiw.execute()


class WhatIUse2:
	def op(self, obj):
		return Adapter(obj).execute()


if __name__ == '__main__':
	human = Human("Bob")
	# Soluzione più comoda
	what_i_use2 = WhatIUse2()
	print(what_i_use2.op(human))
	# Alternativa
	what_i_use = WhatIUse()
	adapt = Adapter(human)
	print(what_i_use.op(adapt))
