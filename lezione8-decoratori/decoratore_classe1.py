import numbers


def ensure(name, validate, doc=None):
	def decorator(classe):
		private_name = "__" + name

		def getter(self):
			return getattr(self, private_name)

		def setter(self, value):
			validate(name, value)
			setattr(self, private_name, value)

		setattr(classe, name, property(getter, setter, doc=doc))
		return classe

	return decorator


def is_in_range(minimum=None, maximum=None):
	assert minimum is not None or maximum is not None

	def is_in_range_checker(name, value):
		if not isinstance(value, numbers.Number):
			raise ValueError("{} must be a number".format(name))
		if minimum is not None and value < minimum:
			raise ValueError("{} {} is too small".format(name, value))
		if maximum is not None and value > maximum:
			raise ValueError("{} {} is too big".format(name, value))

	return is_in_range_checker


def is_not_empty_str(name, value):
	if not isinstance(value, str):
		raise ValueError("{} must be of type str".format(name))
	if not bool(value):
		raise ValueError("{} may not be empty".format(name))


def is_valid_isbn(name, value):
	pass


if __name__ == '__main__':
	@ensure("title", is_not_empty_str)
	@ensure("isbn", is_valid_isbn)
	@ensure("price", is_in_range(1, 10_000))
	@ensure("quantity", is_in_range(0, 1_000_000))
	class Book:
		def __init__(self, title, isbn, price, quantity):
			self.title = title
			self.isbn = isbn
			self.price = price
			self.quantity = quantity

		@property
		def value(self):
			return self.price * self.quantity


	hp1 = Book("Harry Potter e la Pietra Filosofale", "", 10, 500)
	hp2 = Book("Harry Potter e la Camera dei Segreti", "", 12, 800)
	hp3 = Book("Harry Potter e il Prigioniero di Azkaban", "", 17, 2_000)
	hp4 = Book("Harry Potter e il Calice di Fuoco", "", 23, 5_000)
	hp4.price = 25
	print(hp4.value)
	print(hp4.price)
	print(hp4.__dict__)
