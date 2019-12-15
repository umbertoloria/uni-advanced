def coroutine(funz):
	def wrapper(*args, **kwargs):
		x = funz(*args, **kwargs)
		next(x)
		return x

	return wrapper


@coroutine
def default_handler(succ=None):
	while True:
		req = yield
		if req[0] < 0:
			print("Richiesta " + str(
				req) + " gestita da Default_Handler: non è stato possibile gestire la richiesta " + str(req))
		elif succ is not None:
			succ.send(req)


@coroutine
def header_04(succ=None):
	while True:
		req = yield
		if 0 <= req[0] <= 4:
			print("Richiesta " + str(req) + " gestita da Handler_04")
		elif succ is not None:
			succ.send(req)


@coroutine
def header_59(succ=None):
	while True:
		req = yield
		if 5 <= req[0] <= 9:
			print("Richiesta " + str(req) + " gestita da Handler_59")
		elif succ is not None:
			succ.send(req)


@coroutine
def header_gt9(succ=None):
	while True:
		req = yield
		if req[0] >= 9:
			print(
				"Messaggio da Handler_gt9: non è stato possibile gestire la richiesta " + str(
					req) + ". Richiesta modificata")
			req[0] -= req[1]
			new_chain = header_04(
				header_59(
					header_gt9(
						default_handler())))
			new_chain.send(req)
		elif succ is not None:
			succ.send(req)


chain = header_04(
	header_59(
		header_gt9(
			default_handler())))


def funz(richieste):
	for richiesta in richieste:
		chain.send(richiesta)


funz(
	[
		[1, 5],
		[5, 7],
		[4, 10],
		[34, 10],
	]
)
