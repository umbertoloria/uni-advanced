import functools


def coroutine(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		generator = function(*args, **kwargs)
		next(generator)
		return generator

	return wrapper


@coroutine
def ConcreteHandlerOne(successor=None):
	while True:
		request = (yield)
		if 0 < request <= 10:
			print("This is {} handling request '{}'".format("ConcreteHandlerOne", request))
		elif successor is not None:
			successor.send(request)


@coroutine
def ConcreteHandlerTwo(successor=None):
	while True:
		request = (yield)
		if 10 < request <= 20:
			print("This is {} handling request '{}'".format("ConcreteHandlerTwo", request))
		elif successor is not None:
			successor.send(request)


@coroutine
def ConcreteHandlerThree(successor=None):
	while True:
		request = (yield)
		if 20 < request <= 30:
			print("This is {} handling request '{}'".format("ConcreteHandlerThree", request))
		elif successor is not None:
			successor.send(request)


@coroutine
def DefaultHandler(successor=None):
	while True:
		request = (yield)
		print("This is {} telling you that request '{}' has no handler right now".format("DefaultHandler", request))


class Client:
	def __init__(self):
		self.handle = ConcreteHandlerOne(ConcreteHandlerTwo(ConcreteHandlerThree(DefaultHandler(None))))

	def delegate(self, requests):
		for request in requests:
			self.handle.send(request)


# Create a client object
clientOne = Client()

# Create requests to be processed.
requests = [6, 12, 24, 18, 30, 40]

# Send the requests one by one, to handlers as per sequence of handlers defined in the Client class.
clientOne.delegate(requests)

"""Il programma deve stampare:
This is ConcreteHandlerOne handling request '6'
This is ConcreteHandlerTwo handling request '12'
This is ConcreteHandlerThree handling request '24'
This is ConcreteHandlerTwo handling request '18'
This is ConcreteHandlerThree handling request '30'
This is DefaultHandler telling you that request '40' has no handler right now.
"""
