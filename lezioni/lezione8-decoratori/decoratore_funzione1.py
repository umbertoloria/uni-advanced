import functools


def decodeco(func):
	# Decorando la funzione wrapper con functools.wraps, facciamo in modo che __name__ e __docs__ di func siano
	# diciamo "ereditati" da new_func. Questo non è essenziale.
	@functools.wraps(func)
	def new_func(*args, **kwargs):
		new_args = [float(x) for x in args]
		return func(*new_args, **kwargs)
	return new_func

@decodeco
def mean(first, second, *rest):
	numbers = (first, second) + rest
	return sum(numbers) / len(numbers)


print(mean(30, 30, '28'))

