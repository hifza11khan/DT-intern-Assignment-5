# bank_management.py

# Customer Class
class Customer:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")


# Account Class
class Account:
    def __init__(self, account_number, account_type, balance, customer):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        self.customer.display_details()


# SavingsAccount Class (Inheritance)
class SavingsAccount(Account):
    def __init__(self, account_number, balance, customer):
        super().__init__(account_number, "Savings", balance, customer)

    # Polymorphism (overriding)
    def display_account_info(self):
        print(f"Savings Account - Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        self.customer.display_details()


# Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} added.")

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added for {account.customer.name}.")

    def display_customers(self):
        print("Bank Customers:")
        for customer in self.customers:
            customer.display_details()

    def display_accounts(self):
        print("Bank Accounts:")
        for account in self.accounts:
            account.display_account_info()


# Error Handling Example
def main():
    try:
        # Create a bank
        bank = Bank("My Bank")

        # Create a customer
        customer1 = Customer("Ali", "123 Street", "03001234567", "ali@example.com")

        # Create an account for the customer
        account1 = SavingsAccount(101, 5000, customer1)

        # Add the customer and account to the bank
        bank.add_customer(customer1)
        bank.add_account(account1)

        # Show customer and account info
        bank.display_customers()
        bank.display_accounts()

        # Deposit and withdraw money
        account1.deposit(1000)
        account1.withdraw(500)

        # Show updated account info
        account1.display_account_info()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
