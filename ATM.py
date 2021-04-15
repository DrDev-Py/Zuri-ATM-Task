from datetime import datetime
import random 

now = datetime.now()
now = now.strftime("%B %d, %Y.    %H:%M:%S")
print("Today's Date and Time : %s" % now)

database = {} # Contains info of bank customers.


def init():
    print("Welcome to BankPython")

    ownAccount = int(input("Do you have an account with us? 1 - Yes, 2- No \n"))

    if ownAccount == 1:
        login()

    elif ownAccount == 2: 
        register()

    else:
        print("invalid Option")
        init()

def login():
    accountNumberFromUser = int(input("Enter your account number : \n"))
    passwordFromUser = input("Please enter your password : \n")

    for accountNumber, userInfo in database.items():
        if (accountNumber == accountNumberFromUser):
            if (userInfo[3] == passwordFromUser):
                bankOperation(accountNumber, userInfo)
 
    print('invalid account number or password')
    login()      

    #print("Invalid account or password")
         
def register():
    """Creating a profile for a new account holder
    """

    print("**** Please input your details correctly ****")

    first_name = input("What is your first name \n")
    last_name = input("What is your last name? \n")
    email = input("Enter your email \n")
    password = input("Create a password for your account \n")
    

    # Generating account number for new user
    accountNumber = generateAccountNumber()
    

    print("Registration Successful")
    print("*"*14)
    print("This is your new account number %d" % accountNumber)

    # Adding new user to database
    database[accountNumber] = [first_name, last_name, email, password, {"accountBalance":0}, {"complaint":""},]

    """
    Uncomment code below to check for database update
    """
    # print(database[accountNumber])

    login()

def generateAccountNumber():
    print("### Generating New Account Number ###")
    return random.randrange(1111111111,9999999999)
    
def bankOperation( accountNumber, userInfo):
    print("= " * 15)
    print("Welcome %s" %(database[accountNumber])[0])

    operation = int(input("What do you want to do? \n Please select from the options \n 1 - Withdrawal \n 2 - Deposit \n 3 - Make Complaints \n 4 - Exit \n"))

    if operation == 1:
        withdrawalOperation(accountNumber, userInfo)

    elif operation == 2:
        depositOperation(accountNumber, userInfo)

    elif operation == 3:
        makeComplaint(accountNumber, userInfo)

    elif operation == 4:
        exit()

    else:
        print("You have selected an invalid option")
        bankOperation(accountNumber, userInfo)

def withdrawalOperation(accountNumber, userInfo):
    
    withdrawalAmount = int(input("how much do you want to withdraw? \n"))

    currentAccountBalance = ((database[accountNumber])[4])["accountBalance"]

    if (currentAccountBalance < withdrawalAmount) :
        print("insufficient funds")
        bankOperation(accountNumber, userInfo)

    elif (currentAccountBalance >= withdrawalAmount):
        currentAccountBalance = currentAccountBalance - withdrawalAmount

        print("Withdrawal Successful \n Take your cash")
        print("Your account balance is %s" % currentAccountBalance)

        ((database[accountNumber])[4])["accountBalance"] = currentAccountBalance

        bankOperation(accountNumber, userInfo)

def depositOperation(accountNumber, userInfo):
    depositAmount = int(input("how much do you want to deposit? \n"))
    currentAccountBalance = ((database[accountNumber])[4])["accountBalance"]
    currentAccountBalance = currentAccountBalance + depositAmount

    ((database[accountNumber])[4])["accountBalance"] = currentAccountBalance

    print("This is your current account balance : %s" % currentAccountBalance) 

    bankOperation(accountNumber, userInfo)

def makeComplaint(accountNumber, userInfo):
    complaint = str(input('What problems are you facing with our ATM service? \n '))

    ((database[accountNumber])[5])["complaint"] = complaint

    print('Thank You for your feedback we would make the necessary adjustments')

    """
    Uncomment code above to check for database complaint update
    """
    # print(database)

    bankOperation(accountNumber, userInfo)

init()