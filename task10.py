class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        print(self.balance+amount)
Ba1=BankAccount('Polo',900_000)
Ba1.deposit(100)