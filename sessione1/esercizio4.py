# Definire un decoratore di funzione che prende in input un numero variabile di numeri,
# e la trasforma in una funzione che prende in input una lista di valori int, float e str,
# li converte in interi e li invia alla vecchia funzione.


def deco(funz):
	def new_func(lista):
		lista = [int(x) for x in lista if isinstance(x, int) or isinstance(x, float) or isinstance(x, str)]
		return funz(*lista)

	return new_func


@deco
def somma(*nums):
	result = 0
	for num in nums:
		result += num
	return result


# print(somma(1, 2, 3))
print(somma([1.5, 2, "3"]))
