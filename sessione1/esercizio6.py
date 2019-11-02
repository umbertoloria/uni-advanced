class Adapter:

	def __init__(self, obj, adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __str__(self):
		return str(self.obj)


class Lavoratore:

	def __init__(self, nome):
		self.nome = nome

	def __str__(self):
		return "il lavoratore {}".format(self.nome)

	def lavora(self, lavoro):
		return "svolge il seguente {}".format(lavoro)


class Commesso:

	def __init__(self, nome):
		self.nome = nome

	def __str__(self):
		return "il commesso {}".format(self.nome)

	def vende(self, merce):
		return "vende {}".format(merce)


class Cuoco:

	def __init__(self, nome):
		self.nome = nome

	def __str__(self):
		return "il cuoco {}".format(self.nome)

	def cucina(self, pietanza):
		return "cucina {}".format(pietanza)


class Musicista:

	def __init__(self, nome):
		self.nome = nome

	def __str__(self):
		return "il musicista {}".format(self.nome)

	def suona(self, tipo_musica):
		return "suona {}".format(tipo_musica)


# paolo = Commesso("Paolo")
# print(paolo.vende("abiti"))
# veronica = Musicista("Veronica")
# print(veronica.suona("musica pop"))
# antonio = Cuoco("Antonio")
# print(antonio.cucina("una lasagna"))

paolo = Commesso("Paolo")
paolo_ad = Adapter(paolo, {"esegui": paolo.vende})
print(paolo_ad, paolo_ad.esegui("merce"))

veronica = Musicista("Veronica")
veronica_ad = Adapter(veronica, {"esegui": veronica.suona})
print(veronica_ad, veronica_ad.esegui("musica pop"))

antonio = Commesso("Antonio")
antonio_ad = Adapter(antonio, {"esegui": antonio.vende})
print(antonio_ad, antonio_ad.esegui("merce"))
