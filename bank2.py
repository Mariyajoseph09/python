class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_account_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}\n")



def main():
    account = BankAccount(account_number="126786789", name="Amalu", account_type="Savings", balance=500)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. View Account Details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            account.display_account_details()

        elif choice == '4':
            print("Thank you for using the bank system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
