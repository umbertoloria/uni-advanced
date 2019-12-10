# Scrivere anche la funzione ricorsiva myDeepCopy che prende in input una lista che potrebbe contenere al suo interno
# elementi di tipo lista che a loro volta potrebbero contenere elementi di tipo lista, e così via. La funzione
# restituisce la deep copy della lista (no, non si può usare copy.deepcopy)


def myDeepCopy(lista):
	copied = []
	for item in lista:
		if isinstance(item, list):
			copied.append(myDeepCopy(item))
		else:
			copied.append(item)
	return copied


a = ["ciao", ['t', 'a']]
# b = a
# b = list(a)
b = myDeepCopy(a)
b[1].append('o')
b.append("tutti")
print("a", a)
print("b", b)
