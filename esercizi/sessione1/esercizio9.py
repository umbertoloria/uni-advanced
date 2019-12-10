# Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo che restituisce
# il numero di invocazioni del metodo passato come parametro al decorator factory.


def deco(metodo):
	def real_deco(classe):
		old_metodo = getattr(classe, metodo)
		setattr(classe, "_{}_count".format(metodo), 0)

		def get__count():
			return getattr(classe, "_{}_count".format(metodo))

		setattr(classe, "get_{}_count".format(metodo), get__count)

		def new_metodo(*args, **kwargs):
			setattr(
				classe,
				"_{}_count".format(metodo),
				getattr(classe, "_{}_count".format(metodo)) + 1
			)
			return old_metodo(*args, **kwargs)

		setattr(classe, metodo, new_metodo)

		return classe

	return real_deco


@deco("a")
@deco("b")
class X:

	@staticmethod
	def a():
		print("a")
		return 4

	@staticmethod
	def b():
		print("b")


X.a()
X.b()
X.b()

print(X.get_a_count())
print(X.get_b_count())
