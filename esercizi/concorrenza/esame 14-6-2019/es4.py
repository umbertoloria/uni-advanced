import multiprocessing
from random import random


def procTesto(nomi_files, strs, concurrency):
	jobs = multiprocessing.JoinableQueue()
	results = multiprocessing.Queue()
	create_processes(worker, jobs, results, concurrency)
	add_jobs(nomi_files, strs, jobs)
	jobs.join()
	if not validate(results):
		print("ERROR")


def create_processes(worker, jobs, results, concurrency):
	for _ in range(concurrency):
		process = multiprocessing.Process(target=worker, args=(jobs, results))
		process.daemon = True
		process.start()


def add_jobs(nomi_files, strs, jobs):
	for i, couple in enumerate(zip(nomi_files, strs)):
		file = open(couple[0], "r")
		jobs.put((i, couple[1], file.read()))


def worker(jobs, results):
	while True:
		i, needle, haystack = jobs.get()
		results.put((i, haystack.count(needle) > 0))
		jobs.task_done()


def validate(results):
	res = True
	j = 0
	while not results.empty():
		i, result = results.get_nowait()
		print(i, ":", result)
		if i != j:
			res = False
		j += 1
	return res


def rand(a, b):
	diff = b - a + 1
	return a + int((random() * diff) % diff)


if __name__ == "__main__":

	words = ["father", "scatter", "drawing", "dismiss", "autonomy", "net", "horseshoe", "helmet", "willpower", "iron",
	         "pumpkin", "heaven", "bottle", "champion", "head", "national", "check", "relaxation", "important",
	         "biscuit", "response", "remunerate", "magnetic", "bee", "rumor", "health", "retirement", "package",
	         "recover", "rabbit", "humor", "football", "sight", "jaw", "deny", "east", "final", "meadow", "section",
	         "enlarge", "trolley", "stride", "excitement", "link", "cabinet", "beam", "couple", "entitlement",
	         "painter", "notice"]
	nomi_files = []
	for i in range(5):
		nomi_files.append("f" + str(i) + ".txt")
	procTesto(nomi_files, words, 3)
	"""
	for i in range(5):
		f = open("f" + str(i) + ".txt", "w")
		for _ in range(10):
			f.write(words[rand(0, len(words) - 1)])
			f.write(" ")
	"""
