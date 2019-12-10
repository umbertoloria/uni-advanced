from concurrent import futures


def conta(str, files, concurrency):
	futures_set = set()

	with futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
		for i, content in get_jobs(files):
			future = executor.submit(worker, str, i, content)
			futures_set.add(future)
		wait_for(futures_set, str, files)


def get_jobs(files):
	for i, file in enumerate(files):
		f = open(file, "r")
		strsRead = f.read()
		f.close()
		yield i, strsRead


def worker(str, i, content):
	# count = 0
	# for x in content.split(" "):
	#	for x in x.split("\n"):
	#		if x == str:
	#			count += 1
	# return (i, count)
	return (i, content.count(str))


def wait_for(futures_set, str, files):
	for future in futures.as_completed(futures_set):
		result = future.result()
		print("La parola {} è stata trovata nel file {} {} volte".format(str, files[result[0]], result[1]))


def main():
	files = ["f1.txt", "f2.txt", "f3.txt", "f8.txt"]
	conta("ciao", files, 4)


if __name__ == "__main__":
	main()
