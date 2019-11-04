import functools
import sys


class Event:
	KEY_PRESSED = "KeyPressed"
	KEY_RELEASED = "KeyReleased"
	TIMER = "Timer"

	def __init__(self, kind):
		self.kind = kind

	def __str__(self):
		return "Event kind: {}".format(self.kind)


def coroutine(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		generator = function(*args, **kwargs)
		next(generator)
		return generator

	return wrapper


@coroutine
def key_handler(successor=None):
	while True:
		event = yield
		if event.kind == Event.KEY_PRESSED:
			print("Press: {}".format(event))
		elif successor is not None:
			successor.send(event)


@coroutine
def debug_handler(successor, file=sys.stdout):
	while True:
		event = yield
		file.write("*DEBUG*: {}\n".format(event))
		successor.send(event)


@coroutine
def null_handler(successor=None):
	while True:
		event = yield
		if successor is not None:
			successor.send(event)


pipeline = debug_handler(key_handler(null_handler()))

print("Release sent")
print("------------")
pipeline.send(Event(Event.KEY_RELEASED))
print()
print("Pressed sent")
print("------------")
pipeline.send(Event(Event.KEY_PRESSED))
print()
print("Release sent")
print("------------")
pipeline.send(Event(Event.KEY_RELEASED))
