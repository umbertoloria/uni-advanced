# Scrivere una classe con un metodo che aggiunge un attributo di classe alla classe su cui lo chiami.


class ClsBase:

	def addAttr(self, s: str, v):
		if not hasattr(self.__class__, s):
			setattr(self.__class__, s, v)


class ClsChild(ClsBase):
	pass


a = ClsBase()
a.addAttr("ciao", 5)
print(ClsBase.ciao)

b = ClsChild()
b.addAttr("ciao2", 7)
print(ClsChild.ciao2)
