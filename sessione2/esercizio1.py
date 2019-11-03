# Scrivere una funzione ricorsiva che prende in input una lista e un elemento x. Restituisce True se x è contenuto
# nella lista, altrimenti False.


def func(lista, x):
	if not lista:
		return False
	if lista[0] == x:
		return True
	else:
		return func(lista[1:], x)


a = [1, 2, 3, 4, 5]
print(func(a, 1))
print(func(a, 5))
print(func(a, 8))
print(func(a, 2))
