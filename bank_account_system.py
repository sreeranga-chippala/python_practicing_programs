class bank_account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount > 0:
           self.balance=self.balance+amount
           print("Balance after deposition of ",amount,"is ",self.balance)
        else:
            pass
    def withdraw(self,amount):
        if self.balance>=amount:
           self.balance = self.balance - amount
           print("Balance after withdrawl of ",amount,"is ",self.balance)
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("balance is " , self.balance)
name=input("Enter the name of the person:")
balance=float(input("Enter initial balance:"))
account = bank_account(name,balance)

print("\nSelect the choice:\n")
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == '3':
        account.check_balance()

    elif choice == '4':
        print("🙏 Thank you for using our Bank System!")
        break

    else:
        print("Invalid choice. Please try again.")

    again = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if again != 'yes':
        print("Session closed. Have a great day!")
        break