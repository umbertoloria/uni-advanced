# Un esame 27-5-2019 può essere ordinato, spedito, e ricevuto.
# Vogliamo scrivere il suo stato ogni volta che questo cambia.
# Quello è iniziale è ordinato.
# Pacco ha succ e prev
# Lo stato ordinati non è preceduto, e il ricevuto non è seguito.
# L'approccio più semplice sarebbe fare degli if-else.
# Usiamo però l'approccio state-specific!


class Pacco:
	STATI = ("ordinato", "spedito", "ricevuto")
	ORDINATO = 0
	SPEDITO = 1
	RICEVUTO = 2

	d = {
		ORDINATO: (None, SPEDITO),
		SPEDITO: (ORDINATO, RICEVUTO),
		RICEVUTO: (ORDINATO, None)
	}

	def __init__(self):
		self.packageState = Pacco.ORDINATO

	@property
	def packageState(self):
		if self.succ != self._succ:
			return Pacco.RICEVUTO
		elif self.prev != self._prev:
			return Pacco.ORDINATO
		else:
			return Pacco.SPEDITO

	@packageState.setter
	def packageState(self, val):
		if val == Pacco.SPEDITO:
			self.prev = self._prev
			self.succ = self._succ
		elif val == Pacco.ORDINATO:
			self.prev = lambda *args: print("Non posso retrocedere di stato")
			self.succ = self._succ
		elif val == Pacco.RICEVUTO:
			self.prev = self._prev
			self.succ = lambda *args: print("Non posso avanzare di stato")

	def _prev(self):
		self.packageState = self.d[self.packageState][0]

	def _succ(self):
		self.packageState = self.d[self.packageState][1]

	def print_stato(self):
		return Pacco.STATI[self.packageState]


x = Pacco()
print(x.print_stato())

x.succ()
print(x.print_stato())

x.succ()
print(x.print_stato())

x.succ()
print(x.print_stato())

x.prev()
print(x.print_stato())

x.prev()
print(x.print_stato())

x.prev()
print(x.print_stato())

x.prev()
print(x.print_stato())

x.succ()
print(x.print_stato())

x.succ()
print(x.print_stato())

x.succ()
print(x.print_stato())
