class BankAccount:
    def __init__(self,owner,balance):
        
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        
        self.balance=self.balance+amount
        
    def withdraw(self,amount):
        
        self.balance=self.balance-amount
        
    def show_balance(self):
        print(f'Balance: {self.balance} so`m {self.owner}niki')
obyekt1=BankAccount('Odil',10_000_000)
obyekt2=BankAccount('Zarina',30_000_000)
obyekt3=BankAccount('Baxodir',20_000_000)
obyekt1.show_balance()
obyekt1.deposit(20_000_000)
obyekt1.withdraw(5_000)
obyekt1.show_balance()