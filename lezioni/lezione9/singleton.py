class Singleton:
	class __impl:

		def __init__(self):
			pass

		def spam(self):
			return "boh"

	__instance = None

	def __init__(self):
		if Singleton.__instance is None:
			Singleton.__instance = Singleton.__impl()

	def __getattr__(self, attr):
		return getattr(self.__instance, attr)

	def __setattr__(self, attr, value):
		return setattr(self.__instance, attr, value)


s1 = Singleton()
print(id(s1), s1.spam())
s2 = Singleton()
print(id(s2), s2.spam())

s1.x = 5
print(s1.x)
print(s2.x)
