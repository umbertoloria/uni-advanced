# state-sensitive

class Pacco:
	STATI = ("ORDINATO", "SPEDITO", "RICEVUTO")

	ORDINATO = 0
	SPEDITO = 1
	RICEVUTO = 2

	def __init__(self):
		self.__stato = Pacco.ORDINATO

	def prec(self):
		if self.__stato != Pacco.ORDINATO:
			self.__stato -= 1
			self.stampaStato()

	def succ(self):
		if self.__stato != Pacco.RICEVUTO:
			self.__stato += 1
			self.stampaStato()

	def stampaStato(self):
		print(Pacco.STATI[self.__stato])


x = Pacco()

x.succ()

x.succ()

x.succ()

x.prec()

x.prec()

x.prec()

x.prec()

x.succ()

x.succ()

x.succ()
