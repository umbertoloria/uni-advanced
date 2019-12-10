def myFact(current, n, fact):
	if current <= n:
		print("open generator with ", current, n, fact)
		fact *= current
		yield fact
		yield from myFact(current + 1, n, fact)


def myGen(n):
	yield from myFact(1, n, 1)


for f in myGen(5):
	print(f)
