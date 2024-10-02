class Account:
	def __init__(self,amount):
		self.amount= amount

	def getbalance(self):
		return self.amount

	def depositbalance(self,amount):
		self.amount= self.amount+amount

	def withdraw(self, amount):
		self.amount -= amount

