import os
import shelve
import tempfile


class Point:
	__slots__ = ()
	__dbm = shelve.open(os.path.join(tempfile.gettempdir(), "point.db"))

	def __init__(self, x=0, y=0, z=0, color=None):
		self.x = x
		self.y = y
		self.z = z
		self.color = color

	def __getattr__(self, name):
		return Point.__dbm[self.__key(name)]

	def __key(self, name):
		return "{:X}:{}".format(id(self), name)

	def __setattr__(self, name, value):
		Point.__dbm[self.__key(name)] = value


p1 = Point(1, 2, 3, 4)
p2 = Point(31, 32, 33, 34)

print(p1.x, p1.y, p1.z, p1.color)
print(p2.x, p2.y, p2.z, p2.color)
