from libs.logger import logger


class Account:

	def __init__(self, username, password):
		self.__username = username
		self.__password = password

	@property
	def username(self):
		return self.__username

	@property
	def password(self):
		return self.__password

	def __eq__(self, other):
		if isinstance(other, Account):
			return self.username == other.username and self.password == other.password
		else:
			return False

	def __str__(self):
		return "(" + self.username + ", " + self.password + ")"


@logger("account_manager.log")
class AccountManager:
	accounts = {}

	@staticmethod
	def sign_up(account: Account):
		if account.username in AccountManager.accounts.keys():
			return False
		else:
			AccountManager.accounts[account.username] = account
			return True

	@staticmethod
	def sign_in(account: Account):
		if AccountManager.accounts[account.username] is not None:
			return AccountManager.accounts[account.username] == account
		else:
			return False


umberto = Account("umberto", "ciaociao")
michele = Account("michele", "molise")
marco = Account("marco", "des")
print("sign up", umberto, AccountManager.sign_up(umberto))
print("sign up", michele, AccountManager.sign_up(michele))
print("sign up", marco, AccountManager.sign_up(marco))
print("sign in", marco, AccountManager.sign_in(marco))
