class NullHandler:

	def __init__(self, successor=None):
		self.successor = successor

	def handle(self, event):
		if self.successor is not None:
			self.successor.handle(event)


class MouseHandler(NullHandler):
	def handle(self, event):
		if event == "Mouse Button Pressed":
			print(event, "solved")
		else:
			super().handle(event)


class TimerHandler(NullHandler):
	def handle(self, event):
		if event == "Timer":
			print(event, "solved")
		else:
			super().handle(event)


class KeyHandler(NullHandler):
	def handle(self, event):
		if event == "Key Pressed":
			print(event, "solved")
		else:
			super().handle(event)


class DebugHandler(NullHandler):
	def handle(self, event):
		print("*DEBUG*: {}".format(event))
		super().handle(event)


handler1 = DebugHandler(TimerHandler(KeyHandler(MouseHandler(NullHandler()))))
handler1.handle("mouse")
handler1.handle("Mouse Button Pressed")
handler1.handle("Key Pressed")
handler1.handle("Key Pressed")
handler1.handle("Timer")
handler1.handle("altro")
