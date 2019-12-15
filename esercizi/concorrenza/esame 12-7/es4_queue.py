import multiprocessing


def conta(str, files, concurrency):
	jobs = multiprocessing.JoinableQueue()
	create_processes(jobs, str, files, concurrency)
	add_jobs(str, files, jobs)
	jobs.join()


def create_processes(jobs, str, files, concurrency):
	for _ in range(concurrency):
		process = multiprocessing.Process(target=worker, args=(jobs, str, files))
		process.daemon = True
		process.start()


def add_jobs(str, files, jobs):
	for i, file in enumerate(files):
		f = open(file, "r")
		strsRead = f.read()
		f.close()
		jobs.put((i, strsRead))


def worker(jobs, str, files):
	while True:
		i, strRead = jobs.get()
		count = strRead.count(str)
		print("La parola {} è stata trovata nel file {} {} volte".format(str, files[i], count))
		jobs.task_done()


def main():
	files = ["f1.txt", "f2.txt", "f3.txt", "f8.txt"]
	conta("ciao", files, 4)


if __name__ == "__main__":
	main()
