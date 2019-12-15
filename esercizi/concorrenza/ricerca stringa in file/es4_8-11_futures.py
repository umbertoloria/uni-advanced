import concurrent.futures


def cerca(testo, stringa, i):
	for st in testo.split():
		if st == stringa:
			return (True, i)

	return (False, i)


def get_jobs(files, stringhe):
	for i, (file, stringa) in enumerate(zip(files, stringhe)):
		o = open(file, "r")
		s = o.read()

		yield i, s, stringa


def procTesto(files, stringhe, concurrency):
	futures = set()

	with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
		for i, testo, stringa in get_jobs(files, stringhe):
			future = executor.submit(cerca, testo, stringa, i)
			futures.add(future)

		wait_for(futures, files, stringhe)


def wait_for(futures, files, stringhe):
	for future in concurrent.futures.as_completed(futures):
		res = future.result()

		if res[0] == True:
			print("La stringa {} e' presente nel file {}:".format(stringhe[res[1]], files[res[1]]))
		else:
			print("La stringa {} non e' presente nel file {}:".format(stringhe[res[1]], files[res[1]]))


def main():
	files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
	stringhe = ["capra", "st1", "st12", "st11", "sdsdsffsfs"]
	procTesto(files, stringhe, 6)


if __name__ == "__main__":
	main()
