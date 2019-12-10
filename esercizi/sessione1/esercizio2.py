# Scrivere una funzione che prende in input un intero positivo n e restituisce un generatore di interi 1, 3, 6, 10, ...
# In altre parole, l'i-esimo elemento è 0+1+2+...+i-1

def func(n):
	val = 0
	for i in range(n):
		val += i
		yield val


for x in func(10):
	print(x)
