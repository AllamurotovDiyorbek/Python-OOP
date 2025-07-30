class BankAccount:
      def __init__(self,owner,balance):
            self.owner=owner
            self.balance=balance
      def show_balance(self):
            print(f'{self.balance}')
      def get_balance(self):
            return self.balance
bk1=BankAccount("Komil",200_000)
bk2=BankAccount("Laylo",500_000)
bk3=BankAccount("Jamshid",600_000)
bk4=BankAccount("Oqil",200_000)
bk5=BankAccount("Diyor",100_000)
accounts=[bk1,bk2,bk3,bk4,bk5]
c=0
for i in accounts:
      c+=i.balance
print(c)
bk3.get_balance