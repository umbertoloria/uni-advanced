import collections


class MultiplexerSensitive:
	ACTIVE, DORMANT = ("ACTIVE", "DORMANT")

	def __init__(self):
		self.callbacksForEvent = collections.defaultdict(list)
		self.state = MultiplexerSpecific.ACTIVE

	def connect(self, event_name, callback):
		if self.state == MultiplexerSpecific.ACTIVE:
			self.callbacksForEvent[event_name].append(callback)

	def disconnect(self, event_name, callback=None):
		if self.state == MultiplexerSpecific.ACTIVE:
			if callback is None:
				del self.callbacksForEvent[event_name]
			else:
				self.callbacksForEvent[event_name].remove(callback)

	def send(self, event):
		if self.state == MultiplexerSpecific.ACTIVE:
			for callback in self.callbacksForEvent.get(event.name, ()):
				callback(event)


class MultiplexerSpecific:
	ACTIVE, DORMANT = ("ACTIVE", "DORMANT")

	def __init__(self):
		self.callbacksForEvent = collections.defaultdict(list)
		self.state = MultiplexerSpecific.ACTIVE

	@property
	def state(self):
		return MultiplexerSpecific.ACTIVE if self.send == self.__active_send else MultiplexerSpecific.DORMANT

	@state.setter
	def state(self, state):
		if state == MultiplexerSpecific.ACTIVE:
			self.connect = self.__active_connect
			self.disconnect = self.__active_disconnect
			self.send = self.__active_send
		else:
			self.connect = lambda *args: None
			self.disconnect = lambda *args: None
			self.send = lambda *args: None

	def __active_connect(self, event_name, callback):
		self.callbacksForEvent[event_name].append(callback)

	def __active_disconnect(self, event_name, callback=None):
		if callback is None:
			del self.callbacksForEvent[event_name]
		else:
			self.callbacksForEvent[event_name].remove(callback)

	def __active_send(self, event):
		for callback in self.callbacksForEvent.get(event.name, ()):
			callback(event)


class Counter:

	def __init__(self, *names):
		self.anonymous = not bool(names)
		if self.anonymous:
			self.count = 0
		else:
			for name in names:
				if not name.isidentifier():
					raise ValueError("names must be valid identifiers")
				setattr(self, name, 0)

	def __call__(self, event):
		if self.anonymous:
			self.count += event.count
		else:
			count = getattr(self, event.name)
			setattr(self, event.name, count + event.count)


class Event:

	def __init__(self, name, count=1):
		if not name.isidentifier():
			raise ValueError
		self.name = name
		self.count = count


total_counter = Counter()
car_counter = Counter("cars")
commercial_counter = Counter("vans", "trucks")

multiplexer = MultiplexerSpecific()
for event_name, callback in (("cars", car_counter), ("vans", commercial_counter), ("trucks", commercial_counter)):
	multiplexer.connect(event_name, callback)
	multiplexer.connect(event_name, total_counter)


def generate_random_events(n):
	from random import random
	list = []
	for _ in range(n):
		x = int(random() * 3)
		if x == 1:
			list.append(Event("cars", 1))
		elif x == 2:
			list.append(Event("vans", 1))
		else:
			list.append(Event("trucks", 1))
	return list


for event in generate_random_events(100):
	multiplexer.send(event)
	print(
		"After 100 active events: cars={} vans={} trucks={} total={}"
			.format(
			car_counter.cars,
			commercial_counter.vans,
			commercial_counter.trucks,
			total_counter.count
		)
	)

"""
class State_d:

	def __init__(self, imp):
		self.__implementation = imp

	def changeImp(self, new_imp):
		self.__implementation = new_imp

	def __getattr__(self, item):
		return getattr(self.__implementation, item)


class Implementation1:

	def f(self):
		print("Fiddle de dum, Fiddle de dee,")

	def g(self):
		print("Eric the half a bee.")

	def h(self):
		print("Ho ho ho, tee hee hee,")


class Implementation2:

	def f(self):
		print("We're Knights of the Round Table.")

	def g(self):
		print("We dance whene'er we're able.")

	def h(self):
		print("We do routines and chorus scenes")

"""
