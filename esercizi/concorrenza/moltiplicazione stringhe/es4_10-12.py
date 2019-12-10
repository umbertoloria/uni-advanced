from concurrent import futures


def scrivi(s, i):
	l = []
	for _ in range(i):
		l.append(s)
	return l


def wait_for(futures_set):
	for future in futures.as_completed(futures_set):
		print("Questa è la lista prodotta: ", future.result())


def scrivitutti(strs, n, concurrency):
	futures_set = set()
	with futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
		d = n
		for st in strs:
			future = executor.submit(scrivi, st, d)
			futures_set.add(future)
			d = d // 10
		wait_for(futures_set)


if __name__ == "__main__":
	scrivitutti(
		["umberto", "mario", "vincenzo", "rosario"],
		1000,
		3
	)
