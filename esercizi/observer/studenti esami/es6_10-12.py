import collections
import copy
import itertools
import sys
import time
from datetime import datetime

Exam = collections.namedtuple("Exam", "name cfu")


def main():
	historyView = HistoryView()
	liveView = LiveView()
	student = LaureaT_Student(0)
	student.observers_add(historyView, liveView)
	print("Lo studente sta per superare analisi matematica")
	student.add_grade(Exam("analisi matematica", 9), 28)
	print("Lo studente sta per superare asistemi operativi")
	student.add_grade(Exam("sistemi operativi", 6), 20)
	print("Lo studente sta per superare la prova di Inglese")
	student.english_r = True

	for grades, flag, timestamp in historyView.data:
		print("Esami: {}, Inglese: {}, Data: {}"
		      .format(grades,
		              " " if flag == None else "superato" if flag else "non superato",
		              datetime.fromtimestamp(timestamp)), file=sys.stderr)


class Observed:

	def __init__(self):
		self.__observers = set()

	def observers_add(self, observer, *observers):
		for observer in itertools.chain((observer,), observers):
			self.__observers.add(observer)
			observer.update(None)

	def observer_discard(self, observer):
		self.__observers.discard(observer)

	def observsers_notify(self):
		for observer in self.__observers:
			observer.update(self)


class LaureaT_Student(Observed):

	def __init__(self, total_cfu, english_r=False, grade_dict=None):
		super().__init__()
		self.__total_cfu = None
		self.__english_r = None

		self.total_cfu = total_cfu
		self.english_r = english_r
		if grade_dict != None:
			self.grades = grade_dict
		else:
			self.grades = {}

	@property
	def english_r(self):
		return self.__english_r

	@english_r.setter
	def english_r(self, english_r):
		if self.__english_r != english_r:
			self.__english_r = english_r
			self.observsers_notify()

	@property
	def total_cfu(self):
		return self.__total_cfu

	@total_cfu.setter
	def total_cfu(self, total_cfu):
		if self.__total_cfu != total_cfu:
			self.__total_cfu = total_cfu
			self.observsers_notify()

	def add_grade(self, exam, grade):
		if self.grades.get(exam.name) == None:
			self.grades[exam.name] = grade
			self.total_cfu += exam.cfu
			self.observsers_notify()


class HistoryView:

	def __init__(self):
		self.data = []

	def update(self, student):
		if student is not None:
			self.data.append((copy.copy(student.grades), bool(student.english_r), time.time()))


class LiveView:

	def __init__(self):
		self.__oldstate = None

	def update(self, student):
		if self.__oldstate == None:
			pass
		elif self.__oldstate.english_r != student.english_r:
			print("Cambio stato-. lo studente ha appena superato la prova di inglese\n")
		elif self.__oldstate.grades != student.grades:
			print("cambio stato: lo studente ha superato un nuovo esame")
			print("cambio stato: il numero di CFU è: ", student.total_cfu, "\n")
		self.__oldstate = copy.deepcopy(student)


if __name__ == "__main__":
	main()

"""Il programma stampa:

Lo studente sta per superare analisi matematica
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  9 

Lo studente sta per superare asistemi operativi
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  15 

Lo studente sta per superare la prova di Inglese
Cambio stato: lo studente ha appena superato la prova di Inglese

Esami: {}, Inglese: non superato, Data: 2019-12-10 10:54:41.413786
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.474924
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.658306
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.707940
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.908861
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: superato, Data: 2019-12-10 10:54:41.959334

"""
