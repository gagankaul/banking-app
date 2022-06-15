#A banking application for depositing and withdrawing money from savings and checking accounts

#Display welcome message
print("Welcome to the Python First National Bank")


def account_setup():
    """Set up a new savings and checking account and store information in a dictionary"""
    name = input("\nHello, what is your name: ").title()
    savings = float(input("How much money would like to set up your savings account with: "))
    checking = float(input("How much money would like to set up your checking account with: "))
    
    #Build a dictionary that represents specific bank account
    bank_account = {
        "Name": name,
        "Savings": savings,
        "Checking": checking,
    }
    
    return bank_account


def make_deposit(bank_account, type, amount):
    """Add money to a specific type of account"""
    bank_account[type] += amount
    print("\nDeposited $" + str(amount) + " into " + bank_account["Name"] + "'s " + type.lower() + " account.")
    return bank_account[type]


def make_withdrawal(bank_account, type, amount):
    """Withdraw money from a specific type of account"""
    if amount <= bank_account[type]:
        bank_account[type] -= amount
        print("\nWithdrew $" + str(amount) + " from " + bank_account["Name"] + "'s " + type.lower() + "account.")
        return bank_account[type]
    else:
        #Not enough money
        print("\nSorry, insufficient funds. By withdrawing $" + str(amount) + " you will have a negative balance.")


def account_summary(bank_account):
    """Display all key value pairs in the bank account dictionary for the account"""
    print("\nCurrent Account Information")
    for key, value in bank_account.items():
        if key == "Name":
            print(key + ": " + str(value))
        else:
            print(key + ": $" + str(value))


#Create a bank account
my_account = account_setup()

#Main Transaction Loop
running = True
while running:
    #Display current account summary
    account_summary(my_account)

    #Get user input for making a transaction
    trans_acc = input("\nWhat account would you like to access (Savings or Checking): ").title().strip()
    trans_type = input("What type of transaction would you like to make (Deposit or Withdrawal): ").title().strip()
    trans_amt = float(input("How much money: "))

    if trans_acc == "Savings" or trans_acc == "Checking":
        if trans_type == "Deposit":
            make_deposit(my_account, trans_acc, trans_amt)
        elif trans_type == "Withdrawal":
            make_withdrawal(my_account, trans_acc, trans_amt)
        else:
            print("\nSorry, this is an invalid transaction.")
    else:
        print("\nSorry, this account type does not exist.")

    #Check if user wants to transact again
    trans_again = input("Would you like to make another transaction (y/n): ").lower().strip()
    if trans_again != "y":
        print("Thank you. Have a great day!")
        running = False