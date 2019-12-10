class AbstractHandler:
	'''Abstract Handler: inherited by all concrete handlers; throws a NotImplementedError if the concrete
	   handler does not define its own copy of processRequest() method.'''

	def __init__(self, successor):
		''''sets the next handler to local variable "_successor"'''
		self.__successor = successor

	def handle(self, request):
		'''invokes the processRequest() of the current handler; if request is handled, then processing of
		   next request begins; if request cannot be handled by the current handler, it is passed on to the
		   handle() method of the successor handler.'''
		handled = self.processRequest(request)
		if not handled:
			self.__successor.handle(request)

	def processRequest(self, request):
		'''throws a NotImplementedError if the concrete handler does not define its own copy of
		   processRequest() method.'''
		raise NotImplementedError('Must provide implementation in subclass')


class ConcreteHandlerOne(AbstractHandler):
	'''Concrete Handler # 1: Inherits from the abstract handler; overrides the processRequest() method of the
	   AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler'''

	def processRequest(self, request):
		'''Attempt to handle the request; return True if handled'''
		if 0 < request <= 10:
			print("This is {} handling request '{}'".format(self.__class__.__name__, request))
			return True


class ConcreteHandlerTwo(AbstractHandler):
	'''Concrete Handler # 2: Inherits from the abstract handler; overrides the processRequest() method of the
	   AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler'''

	def processRequest(self, request):
		'''Attempt to handle the request; return True if handled'''
		if 10 < request <= 20:
			print("This is {} handling request '{}'".format(self.__class__.__name__, request))
			return True


class ConcreteHandlerThree(AbstractHandler):
	'''Concrete Handler # 2: Inherits from the abstract handler; overrides the processRequest() method of the
	   AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler'''

	def processRequest(self, request):
		'''Attempt to handle the request; return True if handled'''

		if 20 < request <= 30:
			print("This is {} handling request '{}'".format(self.__class__.__name__, request))
			return True


class DefaultHandler(AbstractHandler):
	'''Default Handler: inherits from the abstract handler; overrides the processRequest() method of the
	   AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler'''

	def processRequest(self, request):
		'''Provide an elegant message saying that this request has no handler. returns True to imply that
		   even this request has been handled.'''
		print("This is {} telling you that request '{}' has no handler right now".format(self.__class__, request))
		return True


class Client:
	'''Client: Uses handlers'''

	def __init__(self):
		'''Create the sequence of handlers that you want the requests to follow, and assign the sequence to
		   local variable "handle".'''
		self.handle = ConcreteHandlerOne(ConcreteHandlerTwo(ConcreteHandlerThree(DefaultHandler(None))))

	def delegate(self, requests):
		'''Iterates over requests and sends them, one by one, to handlers as per sequence of handlers
		   defined above.'''
		for request in requests:
			self.handle.handle(request)


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
