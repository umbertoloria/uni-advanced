# Modificare l'esercizio precedente in modo da ignorare le eccezioni dovute ad eventuali conversione impossibili.


def deco(funz):
	def new_func(lista):
		lista_filtrata = []
		for x in lista:
			if isinstance(x, int) or isinstance(x, float) or isinstance(x, str):
				try:
					lista_filtrata.append(int(x))
				except ValueError:
					pass
		return funz(*lista_filtrata)

	return new_func


@deco
def somma(*nums):
	result = 0
	for num in nums:
		result += num
	return result


print(somma([1.5, 2, "3"]))
