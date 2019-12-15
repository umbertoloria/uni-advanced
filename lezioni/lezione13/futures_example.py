import concurrent.futures


def get_results(somme, operazione, concurrency):
	futures_set = set()
	with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
		for job in get_jobs(somme):
			future = executor.submit(worker, job[0], job[1], operazione)
			futures_set.add(future)
		return wait_for(futures_set)


def get_jobs(somme):
	for somma in somme:
		yield somma


def wait_for(futures_set):
	res = []
	for future in concurrent.futures.as_completed(futures_set):
		result = future.result()
		res.append(result)
	return res


def worker(a, b, operation):
	result = str(a) + " " + operation + " " + str(b) + " = "
	if operation == "+":
		result += str(a + b)
	elif operation == "-":
		result += str(a - b)
	else:
		result += "IDK"
	return result


if __name__ == "__main__":
	somme = [(1, 1), (1, 2), (2, 2), (1, 5), (7, 8), (7, 3), (4, 4), (41, 54), (44, 454), (456, 124), (774, 345)]
	risultati = get_results(somme, "-", 12)
	for risultato in risultati:
		print(risultato)
