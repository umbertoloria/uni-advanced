class FW():
	"""
	FW memorizza la parte comune dello stato in SharedState

	"""

	def __init__(self, shared_state: list):
		self._shared_state = shared_state

	"""op aggiunge un oggetto al file, prendendo tutta la parte condivisa dell'auto da shared_state e il resto dal
	parametro its_own_state"""

	def op(self, its_own_state: list, tipo: type, file):
		oggetto = tipo(self._shared_state + its_own_state)
		of = open(file, "w")
		of.write("FW: Nuova macchina con stato condiviso (" + str(self._shared_state) + ") e stato unico (" + str(
			its_own_state) + ")\n")
		print("Il nuovo oggetto di tipo {} è {}:".format(tipo, str(oggetto.state())))
		return oggetto


class FWFactory:
	"""
	Questa classe crea oggetti FW: ne crea uno nuovo se non esiste, altrimenti resituisce uno preesistente
	"""

	_FWDict = {}
	"""inizializza il dizionario degli FW con gli FW passati con initialFW"""

	def __init__(self, initial_fw: list):
		for state in initial_fw:
			self._FWDict[self.get_key(state)] = FW(state)

	def get_key(self, state: list) -> str:
		"""
		restituisce la chiave (stringa) corrispondente ad un certo stato (condiviso)
		"""
		return "_".join(sorted(state))

	def get_FW(self, shared_state: list) -> FW:
		"""
		restituisce un FW con un certo stato o ne crea uno nuovo
		"""
		key = self.get_key(shared_state)
		if not self._FWDict.get(key):
			print("FWFactory: non trovo un FW, ne creo uno nuovo.")
			self._FWDict[key] = FW(shared_state)
		else:
			print("FWFactory: uso un FW esistente.")
		return self._FWDict[key]

	def list_FWs(self):
		# """ stampa numero oggetti FW's e gli stati degli FW's"""
		print("\nFWFactory: ho " + str(len(self._FWDict)) + " oggetti FW:")
		print("\n".join(self._FWDict.keys()))


class Automobile:
	def __init__(self, state: list):
		self._state = state

	def state(self):
		return self._state


def add_car(factory: FWFactory, targa: str, proprietario: str, marca: str, modello: str, colore: str):
	print("\n\nClient: Aggiungo un'automobile.")
	fw = factory.get_FW([marca, modello, colore])
	fw.op([targa, proprietario], Automobile, "automobili.txt")


if __name__ == "__main__":
	"""
	The client code usually creates a bunch of pre-populated flyweights in the
	initialization stage of the application.
	"""

	factory = FWFactory([
		["Chevrolet", "Camaro2018", "rosa"],
		["Mercedes Benz", "C300", "nera"],
		["Mercedes Benz", "C500", "rossa"],
		["BMW", "M5", "rossa"],
		["BMW", "X6", "bianca"],
	])

	factory.list_FWs()

	add_car(
		factory, "DE123AT", "Bob Bab", "BMW", "M5", "rossa")

	add_car(
		factory, "AR324SD", "Mike Smith", "BMW", "X1", "rossa")

	print()

	factory.list_FWs()

"""Il programma stampa :

FWFactory: ho 5 oggetti FW:
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca


Client: Aggiungo un'automobile.
FWFactory: uso un FW esistente.
Il nuovo oggetto di tipo <class '__main__.Automobile'> è ['BMW', 'M5', 'rossa', 'DE123AT', 'Bob Bab']:


Client: Aggiungo un'automobile.
FWFactory: non trovo un FW, ne creo uno nuovo.
Il nuovo oggetto di tipo <class '__main__.Automobile'> è ['BMW', 'X1', 'rossa', 'AR324SD', 'Mike Smith']:


FWFactory: ho 6 oggetti FW:
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca
BMW_X1_rossa

"""
