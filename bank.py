class Bank:
    def __init__(self,balance) -> None:
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 50000
    def check_balnce(self):
        return self.balance
    def diposti(self,amount):
        if amount>500:
            self.balance +=amount
        else:
            print (f"Sorry Sir You Cannot Dipostis lessthen{self.min_withdraw}")
    def withdraw(self,amount):
        if amount>self.min_withdraw and amount < self.balance and amount < self.max_withdraw:
            print(f"Thank You For Using us \nYour Amount is {amount}")
        elif self.balance > self.min_withdraw and self.balance > amount and amount < self.max_withdraw :
            print(f"Minimum withdraw amount is {self.min_withdraw}")
        elif amount>self.max_withdraw:
            print(f"Sorry you cannot withdraw morethen {self.max_withdraw}")
        else:
            print(f"Sorry You Donot have Enough money your balance is {self.balance}")

dbbl = Bank(105000)
dbbl.withdraw(20000000)


