# State-sensitive
class BambinoSensitivo:
	ISCRITTO = 1
	ANNO2 = 2
	ANNO3 = 3
	DIPLOMATO = 4

	def __init__(self):
		self._stato = BambinoSensitivo.ISCRITTO

	@property
	def stato(self):
		return self._stato

	def prev(self):
		if 1 < self._stato < 4:
			self._stato -= 1

	def succ(self):
		if self._stato < 4:
			self._stato += 1

	def salta_anno(self):
		if self._stato < 3:
			self._stato += 2

	def stampa_stato(self):
		if self.stato == BambinoSensitivo.DIPLOMATO:
			print("Il bambimo è diplomato")
		else:
			print("Il bambino è all'anno {}".format(self.stato))


# State-specific
class BambinoSpecifico:
	ISCRITTO = 1
	ANNO2 = 2
	ANNO3 = 3
	DIPLOMATO = 4

	def empty(self):
		pass

	def becomeISCRITTO(self):
		self._stato = BambinoSpecifico.ISCRITTO

	def becomeANNO2(self):
		self._stato = BambinoSpecifico.ANNO2

	def becomeANNO3(self):
		self._stato = BambinoSpecifico.ANNO3

	def becomeDIPLOMATO(self):
		self._stato = BambinoSpecifico.DIPLOMATO

	def stampaANNOX(self):
		print("Il bambimo è all'anno {}".format(self.stato))

	def stampaDIPLOMATO(self):
		print("Il bambimo è diplomato")

	def __init__(self):
		self.stato = BambinoSensitivo.ISCRITTO

	@property
	def stato(self):
		return self._stato

	@stato.setter
	def stato(self, stato):
		self._stato = stato
		if stato == BambinoSpecifico.DIPLOMATO:
			self.stampa_stato = BambinoSpecifico.stampaDIPLOMATO
		else:
			self.stampa_stato = BambinoSpecifico.stampaANNOX

		if stato == BambinoSpecifico.ISCRITTO:
			self.prev = BambinoSpecifico.empty
			self.succ = BambinoSpecifico.becomeANNO2
		elif stato == BambinoSpecifico.ANNO2:
			self.prev = BambinoSpecifico.becomeISCRITTO
			self.succ = BambinoSpecifico.becomeANNO3
		elif stato == BambinoSpecifico.ANNO3:
			self.prev = BambinoSpecifico.becomeANNO2
			self.succ = BambinoSpecifico.becomeDIPLOMATO
		elif stato == BambinoSpecifico.ANNO3:
			self.prev = BambinoSpecifico.empty
			self.succ = BambinoSpecifico.empty

	def prev(self):
		pass

	def succ(self):
		pass

	def stampa_stato(self):
		pass


# x = BambinoSensitivo()
x = BambinoSpecifico()
x.succ()
x.succ()
x.prev()
x.succ()
x.prev()
x.stampa_stato()
