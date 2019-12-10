# Scrivere una funzione che prende in input una lista e restituisce tutte le permutazioni dei suoi elementi.

def func(l):
	if len(l) == 1:
		return l
	else:
		result = []
		for i in range(0, len(l)):
			lMenoElem = l[:]
			lMenoElem.pop(i)
			for comb in func(lMenoElem):
				result.append(l[i] + comb)
		return result


a = ["c", "a", "s", "a"]
print("input: ", a)
print("output:")
for l in func(a):
	print(l)
