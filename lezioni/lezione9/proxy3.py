from tkinter import Image


class ImageProxy:

	def __init__(self, image_class, width=None, height=None, filename=None):
		assert (width is not None and height is not None) or filename is not None
		self.Image = image_class
		if filename is not None:
			self.load(filename)
		else:
			self.commands = [(self.Image, width, height)]

	def load(self, filename):
		self.commands = [(self.Image, None, None, filename)]

	def set_pixel(self, x, y, color):
		self.commands.append((self.Image.set_pixel, x, y, color))

	def line(self, x0, y0, x1, y1):
		self.command.append((self.Image.line, x0, y0, x1, y1))

	def rectangle(self, x0, y0, x1, y1, outline=None, fill=None):
		self.command.append((self.Image.rectangle, x0, y0, x1, y1, outline, fill))

	def ellipse(self, x0, y0, x1, y1, outline=None, fill=None):
		self.command.append((self.Image.ellipse, x0, y0, x1, y1, outline, fill))

	def save(self, filename=None):
		command = self.commands.pop(0)
		function, *args = command
		image = function(*args)
		for command in self.commands:
			function, *args = command
			function(image, *args)
		image.save(filename)
		return image


YELLOW = Image.color_for_name("yellow")
CYAN = Image.color_for_name("cyan")
BLUE = Image.color_for_name("blue")
RED = Image.color_for_name("red")
BLACK = Image.color_for_name("black")

img = ImageProxy(Image.Image, 300, 60)
img.rectangle(0, 0, 299, 59, fill=YELLOW)
img.ellipse(0, 0, 299, 59, fill=CYAN)
img.ellipse(60, 20, 120, 40, BLUE, RED)
img.ellipse(180, 20, 240, 40, BLUE, RED)
img.rectangle(180, 32, 240, 41, fill=CYAN)
img.line(181, 32, 239, 32, BLUE)
img.line(140, 50, 160, 50, BLACK)
img.save("img.png")
