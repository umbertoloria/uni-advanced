class WhatIHave:
	def g(self):
		pass

	def h(self):
		pass


class WhatIWant:
	def f(self):
		pass


# Essenzialmente sembra un WhatIWant (in realtà lo è) e contiene un WhatIHave
class Adapter(WhatIWant):
	def __init__(self, what_i_have):
		self.what_i_have = what_i_have

	def f(self):
		self.what_i_have.g()
		self.what_i_have.h()


class WhatIUse:
	def op(self, what_i_want):
		what_i_want.f()


class WhatIUse2:
	def op(self, what_i_have):
		Adapter(what_i_have).f()


what_i_have = WhatIHave()

# Soluzione più comoda
what_i_use2 = WhatIUse2()
what_i_use2.op(what_i_have)

# Alternativa
what_i_use = WhatIUse()
adapt = Adapter(what_i_have)
what_i_use.op(adapt)
