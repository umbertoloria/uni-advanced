def sommatoria_gen(i, n, tmp):
	if i <= n:
		yield i + tmp
		yield from sommatoria_gen(i + 1, n, i + tmp)


def sommatoria(n):
	yield from sommatoria_gen(1, n, 0)


for x in sommatoria(5):
	print(x)
