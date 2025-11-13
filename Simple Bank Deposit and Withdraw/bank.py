balance = 0
account_no = 1234567890  # Example account number
data = None          # define before loop

class Bank:
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

    def deposit(self):
        global balance
        acc_no = int(input("Enter your Account Number: "))
        if acc_no == account_no:
            amount = int(input("Enter the amount to deposit: "))
            balance += amount
            print("Deposited Successfully !!!")
            print("Your Current Balance: ", balance)
        else:
            print("Invalid Account Number")

    def withdraw(self):
        global balance
        acc_no = int(input("Enter your Account Number: "))
        if acc_no == account_no:
            amount = int(input("Enter the withdraw amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdraw Successful !!!")
                print("Your Current Balance: ", balance)
            else:
                print("Insufficient Balance !!!")
        else:
            print("Invalid Account Number")

    def balance_check(self):
        global balance
        acc_no = int(input("Enter your Account Number: "))
        if acc_no == account_no:
            print("Your Current Balance: ", balance)
            print("Thank You !!!!!")
        else:
            print("Invalid Account Number")

while True:
    print("=====> 1. Create An account ")
    print("=====> 2. Deposit Amount")
    print("=====> 3. Withdraw an Amount")
    print("=====> 4. Balance Check ")
    print("=====> 5. Exit")

    request = int(input("Enter your choice (1-5): "))

    if request == 1:
        name = input("Enter Your name: ")
        phone = input("Enter Your Phone number: ")
        if len(phone) == 10:
            email = input("Enter Your Email: ")
            password = input("Enter your password: ")
            if len(password) >= 4:
                data = Bank(name, phone, email, password)
                print(f"Account Created Successfully! Your Account No is: {account_no}")
            else:
                print("Password length minimum 4 characters")
        else:
            print("Phone number should be 10 digits")
    elif request == 2:
        if data:
            data.deposit()
        else:
            print("Please create an account first!")
    elif request == 3:
        if data:
            data.withdraw()
        else:
            print(" Please create an account first!")
    elif request == 4:
        if data:
            data.balance_check()
        else:
            print(" Please create an account first!")
    elif request == 5:
        print("Exited Successfully !!!")
        break
    else:
        print("Invalid Option! Try again.")


                
                  
            
    
        
        
