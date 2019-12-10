# Scrivere una classe che conta il numero di invocazioni ai metodi.


def deco(metodo):
	def real_deco(classe):
		old_metodo = getattr(classe, metodo)
		if not hasattr(classe, "__count"):
			setattr(classe, "__count", 0)

		def get_count():
			return getattr(classe, "__count")

		setattr(classe, "get_count".format(metodo), get_count)

		def new_metodo(*args, **kwargs):
			setattr(
				classe, "__count",
				getattr(classe, "__count") + 1
			)
			return old_metodo(*args, **kwargs)

		setattr(classe, metodo, new_metodo)

		return classe

	return real_deco


@deco("b")
@deco("a")
class X:

	@staticmethod
	def a():
		print("a")
		return 4

	@staticmethod
	def b():
		print("b")


X.a()
X.a()
X.b()
X.b()
X.b()

print(X.get_count())
