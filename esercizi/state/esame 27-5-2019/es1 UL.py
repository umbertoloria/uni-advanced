#  Un esame 27-5-2019 può essere ordinato, spedito, e ricevuto.
#  Vogliamo scrivere il suo stato ogni volta che questo cambia.
#  Quello è iniziale è ordinato.
#  Pacco ha succ e prev
#  Lo stato ordinati non è preceduto, e il ricevuto non è seguito.
#  L'approccio più semplice sarebbe fare degli if-else. Usiamo però l'approccio state-specific


class Pacco:
	STATI = ("ordinato", "spedito", "ricevuto")
	ORDINATO = 0
	SPEDITO = 1
	RICEVUTO = 2

	def __init__(self):
		self.stato = Pacco.ORDINATO

	@property
	def stato(self):
		if self.prev == self._diventa_spedito:
			return Pacco.RICEVUTO
		elif self.prev == self._diventa_ordinato:
			return Pacco.SPEDITO
		else:
			return Pacco.ORDINATO

	@stato.setter
	def stato(self, val):
		if val == Pacco.ORDINATO:
			self.prev = lambda *args: print("Non posso retrocedere di stato")
			self.succ = self._diventa_spedito
		elif val == Pacco.SPEDITO:
			self.prev = self._diventa_ordinato
			self.succ = self._diventa_ricevuto
		elif val == Pacco.RICEVUTO:
			self.prev = self._diventa_spedito
			self.succ = lambda *args: print("Non posso avanzare di stato")

	def _diventa_ordinato(self):
		self.stato = Pacco.ORDINATO

	def _diventa_spedito(self):
		self.stato = Pacco.SPEDITO

	def _diventa_ricevuto(self):
		self.stato = Pacco.RICEVUTO

	def print_stato(self):
		return Pacco.STATI[self.stato]


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
