def logger(filename):
	fp = open(filename, "w")

	def deco_classe(classe):
		for func_name, func_call in classe.__dict__.items():
			is_callable = False
			real_callable = None
			try:
				if callable(func_call):
					real_callable = func_call
				else:
					real_callable = func_call.__func__
				is_callable = True
			except AttributeError:
				pass
			if is_callable:

				def deco_func_wrap(function_name, function_call, log_result=True):
					def deco_func(*args, **kwargs):
						from datetime import datetime
						before = datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
						result = function_call(*args, **kwargs)
						after = datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
						log_str = str(before) + "\n"
						log_str += function_name + "("
						for arg in args:
							log_str += "\"" + str(arg) + "\""
							log_str += ", "
						for kwarg_key, kwarg_value in kwargs.items():
							log_str += str(kwarg_key)
							log_str += "="
							log_str += "\"" + str(kwarg_value) + "\""
							log_str += ", "
						if log_str.endswith(", "):
							log_str = log_str[:-2]
						log_str += ")"
						if log_result:
							log_str += ": \"" + str(result) + "\""
						log_str += "\n" + str(after)
						log_str += "\n\n"
						fp.write(log_str)
						return result

					return deco_func

				setattr(classe, func_name, deco_func_wrap(func_name, real_callable, func_name != "__init__"))
		return classe

	return deco_classe


# def logger(filename):
# 	fp = open(filename, "w")
#
# 	def deco_classe(classe):
# 		for key, value in classe.__dict__.items():
# 			if callable(value) and key != "__init__":
# 				def deco_func(func):
# 					fp.write("calling to " + key + "\n")
# 					return func
#
# 				setattr(classe, key, deco_func(value))
# 		return classe
#
# 	return deco_classe

if __name__ == "__main__":

	@logger("file.log")
	class X:

		def __init__(self, x, y):
			self._x = x
			self._y = y

		@property
		def x(self):
			return self._x

		def ciao(self, extra1="", extra2=""):
			for _ in range(5_000):
				pass
			return "ciao " + extra1 + extra2

		def addio(self, extra=""):
			return "addio " + extra


	a = X(1, 2)
	print(a.ciao("a te", "e a me"))
	print(a.addio("addio amici addio"))
	print(a.x)
	print(a._x)
# il logger non intralcia l'accesso privato di a._x
