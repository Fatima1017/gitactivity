class Account:
	def __init__(self,amount):
		self.amount= amount

	def getbalance(self):
		return self.amount

	def depositbalance(self,amount):
		self.amount= self.amount+amount

	def withdraw(self, amount):
		self.amount -= amount

o1= Account(2000)
print("amount:", o1.amount)
