class ATM:
    def __init__(self , initial_balance=100000, pin="3456"):
         self.balance = initial_balance
         self.pin = pin
    def verify_pin(self, entered_pin):
             return self.pin == entered_pin
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def change_pin(self, pin):
        pin=input ("Please enter your old pin: ")
        if self. pin==pin:
            pin=input("Please enter your new pin: ")

            self. pin = pin
            return True
        else:
            print("Incorrect Pin")
        return False
def start():
        atm = ATM()
        attempts = 3
        print ("Welcome!")

        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if atm. verify_pin(entered_pin):
                print("PIN accepted.")
                break
            else:
                 attempts -= 1
                 print(f"Incorrect PIN. You have (attempts) attempts remaining.")
        else:
             print("Too many incorrect attempts. Card blocked.")
             return
        
        while True:
            print("\nATM Menu; ")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change Pin")
            print("5. Exit")
            choice = input("please enter the number of your choice: ")
            match choice:
                case '1':
                    print(f"Your current balance is: ₹{atm. check_balance()}")
                case'2':
                    amount = int(input("Enter amount to deposit: *"))
                    if atm. deposit (amount):
                        print (f"Successfully deposited ₹{amount}. Current balance: ₹{atm.check_balance()}")
                    else:
                        print("Invalid deposit amount. Please try again.")
                case '3':
                    amount = int(input("Enter amount to withdraw: ₹"))

                    if atm.withdraw(amount):
                        print(f"Successfully withdrew ₹{amount}. Current balance: ₹{atm. check_balance()}")
                        print("Please collect your cash.")
                    else:
                        print("Insufficient funds or invalid withdrawal amount.")
                case'4':
                    if atm. change_pin(atm.pin):
                        print("Pin changed Sucessfully")
                    else:
                        print("Pin change is Unsuccessful")
                case '5':
                    print("Thank you for using the ATM.")
                    break
                case _:
                    print("Please enter a valid number of your choice")
start()