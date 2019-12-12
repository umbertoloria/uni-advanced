import functools
import re


def coroutine(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		generator = function(*args, **kwargs)
		next(generator)
		return generator

	return wrapper


@coroutine
def selezionatore(n, ricevitore):
	while True:
		txt = yield
		for word in re.findall(r"\w+", txt):
			if len(word) > n:
				ricevitore.send(word)


@coroutine
def archivisita(archivio):
	while True:
		archivio.write((yield))
		archivio.write(" ")


file = open("boh.txt", "w")

s = selezionatore(4, archivisita(file))

s.send("ciao a tutti sono ummberto")

file.close()
