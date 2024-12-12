from select import select


class Bank:
    Bank_name="CANARA BANK"
    def __init__(self,Name,age,accountNo,balance=0):
        self.N=Name
        self.A=age
        self.no=accountNo
        self.b=balance

    def deposit(self,amount):
        if b < 0
            self.b = b + amount
            return f"the deposited amount is:{amount}, and the current balance is{self.b}"
        else:
            print("The deposited amount must be greater than Zero")


    def withdrew(self,amount):
        if amount > 0:
            if amount <= self.b:
                self.b = self.b- amount
                return f"withdrew amount:{amount}, and the balance is{self.b}"
            else:
                print("insufficent balane")
        else:
            print("the withdrewal done!!")


    def display(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}\n")
