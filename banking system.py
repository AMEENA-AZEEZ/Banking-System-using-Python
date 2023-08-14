# Create a dictionary to store user accounts
accounts = {
    'Ameena': {'password': 'pass123', 'balance': 1000},
    'Aayisha': {'password': 'pass456', 'balance': 1500}
}
def login(username, password):
    if username in accounts and accounts[username]['password'] == password:
        return True
    return False
def deposit(username, amount):
    if amount > 0:
        accounts[username]['balance'] += amount
        return True
    return False

def withdraw(username, amount):
    if amount > 0 and accounts[username]['balance'] >= amount:
        accounts[username]['balance'] -= amount
        return True
    return False


while True:
    print("Welcome to the Basic Banking System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if login(username, password):
        print("Login successful!")
        while True:
            print("\nOptions:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")
            choice = input("Select an option: ")

            if choice == '1':
                print(f"Your balance: ${accounts[username]['balance']}")
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                if deposit(username, amount):
                    print("Deposit successful!")
                else:
                    print("Invalid amount.")
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                if withdraw(username, amount):
                    print("Withdrawal successful!")
                else:
                    print("Insufficient funds or invalid amount.")
            elif choice == '4':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Invalid username or password. Please try again.")
