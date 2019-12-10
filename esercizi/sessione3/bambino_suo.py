# State-specific: non esiste a variabile privata stato. Si capisce dai metodi
class Bambino:
	STATI = ("iscritto", "2 anno", "3 anno", "diplomato")
	ISCRITTO = 0
	IIANNO = 1
	IIIANNO = 2
	DIPLOMATO = 3

	def __init__(self):
		self.stato_bimbo = Bambino.ISCRITTO

	@property
	def stato_bimbo(self):
		if self.succ != self._succ:
			return Bambino.DIPLOMATO
		if self.pred != self._pred:
			return Bambino.ISCRITTO
		if self.succ == self._succ and self.salta_anno != self._salta_anno:
			return Bambino.IIIANNO
		return Bambino.IIANNO

	@stato_bimbo.setter
	def stato_bimbo(self, new_state):
		if new_state == Bambino.IIANNO:
			self.succ = self._succ
			self.salta_anno = self._salta_anno
			self.pred = self._pred
		if new_state == Bambino.IIIANNO:
			self.salta_anno = lambda *args: print("** il bambino è già al terzo anno")
			self.succ = self._succ
			self.pred = self._pred
		if new_state == Bambino.ISCRITTO:
			self.pred = lambda *args: print("** il bambino è iscritto")
			self.succ = self._succ
			self.salta_anno = self._salta_anno
		if new_state == Bambino.DIPLOMATO:
			self.pred = self._pred
			self.succ = lambda *args: print("** il bambino si è diplomato")
			self.salta_anno = lambda *args: print("** il bimbo si è diplomato")

	def _succ(self):
		self.stato_bimbo += 1

	def _pred(self):
		self.stato_bimbo -= 1

	def _salta_anno(self):
		self.stato_bimbo += 2

	def stampa_stato(self):
		print("Il bambino è nello stato", Bambino.STATI[self.stato_bimbo])


a = Bambino()
a.stampa_stato()  # iscritto

a.pred()
a.stampa_stato()  # iscritto

a.succ()
a.stampa_stato()  # 2 anno

a.pred()
a.stampa_stato()  # iscritto

a.succ()
a.stampa_stato()  # 2 anno

a.succ()
a.stampa_stato()  # 3 anno

a.succ()
a.stampa_stato()  # diplomato

a.succ()
a.stampa_stato()  # diplomato
