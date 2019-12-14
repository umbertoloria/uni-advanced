import itertools
import time


class Observed:

	def __init__(self):
		self.__observers = set()

	def observers_add(self, observer, *observers):
		for observer in itertools.chain((observer,), observers):
			self.__observers.add(observer)
			observer.update(self)

	def observer_discard(self, observer):
		self.__observers.discard(observer)

	def observer_notify(self):
		for observer in self.__observers:
			observer.update(self)


class HistoryView:

	def __init__(self):
		self.data = []

	def update(self, model):
		self.data.append((str(model), time.time()))

	def status(self):
		for data in self.data:
			print(data[0], "in", data[1])


class LiveView:

	def __init__(self, length=0):
		self.length = length

	def update(self, model):
		print("nuovo stato:", model)


class Osservato(Observed):

	def __init__(self):
		super().__init__()
		self.__x = None

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		if self.__x != value:
			self.__x = value
			self.observer_notify()

	def __str__(self):
		return str(self.__x)


history_view = HistoryView()
live_view = LiveView()
model = Osservato()

model.observers_add(history_view, live_view)

model.x = 5
model.x = 10
model.x = 15

history_view.status()
