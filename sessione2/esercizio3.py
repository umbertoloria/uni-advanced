# Scrivere la classe MyDictionary che implementa gli operatori di dict:
#     d[key]
#     d[key] = value
#     del d[key]
#     key in d
#     key not in d
#     d1 == d2
#     d1 != d2
# MyDictionary deve avere *solo* una variabile di istanza e questa deve essere di tipo lista.
# Per rappresentare le coppie, dovete usare la classe MyPair che ha due variabili di istanza (key e value)
# e i metodi getKey, getValue, setKey e setValue.


class MyPair:

	def get_key(self):
		return self.key

	def set_key(self, key):
		self.key = key

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value


class MyDict:

	def __init__(self):
		self.pairs = []

	def __getitem__(self, key):
		for pair in self.pairs:
			if pair.get_key() == key:
				return pair.get_value()
		return None

	def __setitem__(self, key, value):
		for pair in self.pairs:
			if pair.get_key() == key:
				pair.set_value(value)
				return
		new_pair = MyPair()
		new_pair.set_key(key)
		new_pair.set_value(value)
		self.pairs.append(new_pair)

	def __delitem__(self, key):
		i = 0
		for pair in self.pairs:
			if pair.get_key() == key:
				self.pairs.pop(i)
				return
			i += 1

	def __contains__(self, key):
		for pair in self.pairs:
			if pair.get_key() == key:
				return True
		return False

	def __eq__(self, other):
		for pair in self.pairs:
			if other[pair.get_key()] != pair.get_value():
				return False
		for pair in other.pairs:
			if self[pair.get_key()] != pair.get_value():
				return False
		return True


d1 = MyDict()
print("emanuele value  :", d1["emanuele"])

d1["emanuele"] = 13
print("emanuele value  :", d1["emanuele"])

del d1["emanuele"]
print("emanuele value  :", d1["emanuele"])

print("emanuele key in :", "emanuele" in d1)

d2 = MyDict()

d1["bob"] = 17
d2["bob"] = 17

d1["alessio"] = 28
d2["alessio"] = 28

d1["biagio"] = 47
d2["biagio"] = 47

print("d1 == d2        :", d1 == d2)
