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


class Adapter:

	def __init__(self, obj, adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __str__(self):
		return str(self.obj)


if __name__ == '__main__':
	objects = [Computer("Asus")]
	synth = Synthesizer("Moog")
	objects.append(Adapter(synth, {"execute": synth.play}))
	human = Human("Bob")
	objects.append(Adapter(human, {"execute": human.speak}))
	for obj in objects:
		print("{} {}".format(str(obj), obj.execute()))
