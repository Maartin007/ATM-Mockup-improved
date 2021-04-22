
import datetime
import random

#This Function asks the user if they already a customer
def init():
    print("Welcome to Zuri Bank PLC")

    # This displays the date and time
    now = datetime.datetime.now()
    print ("The current date and time is" , now.strftime("%Y-%m-%d %H:%M:%S"))

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option, Please select 1 or 2")


# This is the Login fuction
def login():
    print(" You can Log into your account here")

    User_names = ["martin" , "ebuka" , "okolie"]
    passwords = ["Badolee11" , "Snipper77" , "Magnet001"]

    print ("Please input your Username")
    username = input("")
    if username in User_names:
        print("Please input your password\n")
        password =  input("")
        if password in passwords:
            print("Your login was succesful, Welcome" ,username )
        else:
            print("Your password is Incorrect, Please log in again")
        
    else:
        print("You do not have an account with us please register")
        register()


accountBalance = 5000
# This asks the customer to select an option
def transaction():
    preferedOption = int(input("What do you want to do today? "))
    print("1. Withdraw cash \n2. Deposit Cash \n3. Report an issue")
    

# This is the code for Withdrawal
    if (preferedOption == 1):
        withdrawal = int (input("How much do you want to withdraw? \n"))
        print("Please take your cash")

# This is the code for Deposit
    elif (preferedOption == 2):
        depositAmount = int(input("How much would you to deposit? \n"))
        print("Your current balance is ", accountBalance + depositAmount)

# This is the code for Complain
    elif(preferedOption == 3):
        print("Do you want to report an issue?")
        report = str (input("What issue would you like to report?: "))
        print("Your Issue has been reported, Thank you for contacting us")

# This executes if the user does not input the approprite option
    else:
        while (int(input!= 1 or 2 or 3)):
            print("Please input 1, 2 or 3 when the program runs again")
            transaction()



#This function is for registration
def register():
    print("You can Register here")
    print("Please Input a username")
    user_names = []
    username = input()
    user_names.append(username)
    print("Please enter your password")
    passwords = []
    password = input()
    passwords.append(password)
    
    print("Your Account Has been created")
    generatedNumbers()
    transaction()

# This function generates account numbers    
def generatedNumbers():
    account_number = random.randrange (1,50) 
    print (f"Your account number is account_number  {account_number:010}")
    print("Make sure you keep it safe")
        




init()
