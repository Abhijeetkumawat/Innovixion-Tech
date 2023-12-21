def create_account():
    account_holder_name = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance: "))
    return account_holder_name, initial_balance

def check_balance(balance):
    print(f"Current balance: ${balance}")

def deposit(balance):
    deposit_amount = float(input("Enter the deposit amount: "))
    if deposit_amount > 0:
        balance += deposit_amount
        print(f"Deposited ${deposit_amount}. New balance: ${balance}")
    else:
        print("Invalid deposit amount. Please enter a positive value.")
    return balance

def withdraw(balance):
    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    if withdrawal_amount > 0 and withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print(f"Withdrew ${withdrawal_amount}. New balance: ${balance}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
    return balance

account_holder_name, initial_balance = create_account()
balance = initial_balance

while True:
    print("\nBank Account Management System")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance(balance)

    elif choice == "2":
        balance = deposit(balance)

    elif choice == "3":
        balance = withdraw(balance)

    elif choice == "4":
        print("Exiting the Bank Account Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
