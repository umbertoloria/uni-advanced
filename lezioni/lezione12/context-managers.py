"""

with open("some_file", "w") as opened_file:
	opened_file.write("Hola!")

SONO EQUIVALENTI

file = open("some_file", "w")
try:
	file.write("Hola!")
finally:
	file.close()

"""


class File:

	def __init__(self, file_name, method):
		self.file_obj = open(file_name, method)

	def __enter__(self):
		return self.file_obj

	def __exit__(self, exc_type, exc_val, exc_tb):
		# return True: un'eventuale eccezione viene gestita graziosamente, altrimenti viene rilanciata da WITH AS
		self.file_obj.close()


with File("demo.txt", "w") as opened_file:
	opened_file.write("Hola!")

from contextlib import contextmanager


@contextmanager
def open_file(filename, method):
	f = open(filename, method)
	try:
		yield f
	finally:
		f.close()


with open_file("demo2.txt", "w") as opened_file:
	opened_file.write("Hola amigo!")
