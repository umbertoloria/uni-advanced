import multiprocessing


def get_results(somme, operazione, concurrency):
	jobs = multiprocessing.JoinableQueue()
	results = multiprocessing.Queue()
	create_processes(jobs, results, concurrency)
	add_jobs(somme, operazione, jobs)
	jobs.join()
	return summarize(results)


def create_processes(jobs, results, concurrency):
	for _ in range(concurrency):
		process = multiprocessing.Process(target=worker, args=(jobs, results))
		process.daemon = True
		process.start()


def add_jobs(somme, operation, jobs):
	for somma in somme:
		jobs.put((somma[0], somma[1], operation))


def worker(jobs_jq, results_q):
	while True:
		a, b, operation = jobs_jq.get()
		result = str(a) + " " + operation + " " + str(b) + " = "
		if operation == "+":
			result += str(a + b)
		elif operation == "-":
			result += str(a - b)
		else:
			result += "IDK"
		results_q.put(result)
		jobs_jq.task_done()


def summarize(results_q):
	res = []
	while not results_q.empty():
		result = results_q.get()
		res.append(result)
	return res


if __name__ == "__main__":
	somme = [(1, 1), (1, 2), (2, 2), (1, 5), (7, 8), (7, 3), (4, 4), (41, 54), (44, 454), (456, 124), (774, 345)]
	risultati = get_results(somme, "-", 12)
	for risultato in risultati:
		print(risultato)
