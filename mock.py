name = input("What is your name? \n")
allowedusers = ("Olaide", "Tolu" , "Adebayo")
allowedpassword  = ("passwordOlaide", "passwordTolu", "passwordAdebayo")
atm = ("Genesis bank")

import datetime

e = datetime.datetime.now()




if(name in allowedusers):
    password = input("Your password? \n")
    userid = allowedusers.index(name)

    if(password == allowedpassword[userid]):

        print("%s" % atm)
        
        print(e.strftime("%Y-%m-%d %H:%M:%S"))
        
        print("Welcome %s" % name)
        
        print("These are the available options:")
        print("1. Withrawal")
        print("2. cash deposit")
        print("3. complaint")

        selectedoption = int(input("Please select an option:"))

        print(selectedoption == 1)
        if(selectedoption == 1):
            print("How much would you like to withdraw?")
            print("1. 10,000")
            print("2. 20,000")
            print("3. 25,000")
            
            verifiedoption = int(input("Please select an option:"))

    
            if(verifiedoption == 1):
                print("Take your cash")
                
            if(verifiedoption == 2):
                print("Take your cash")

            if(verifiedoption == 3):
                print("Insufficient fund")
                

        elif(selectedoption == 2):
            print("How much would you like to deposit?")
            print("1. 5,000")
            print("2. 25,000")
            print("3. 50,000")
            print("4. Others")

            verification = int(input("Please select an option:"))

            if(verification == 1):
                print("Successful, Current balance = 6,000")

            if(verification == 2):
               print("Successful, Current balance = 26,000")
            if(verification == 3):
                print("Successful, Current balance = 51,000")
            if(verification == 4):
                deposit = input("Amount to be deposited. \n")
                print("successful deposit")
                            
                  

        elif (selectedoption == 3):

            report = input("What issue will you like to report? \n")

            print("Thank you for contacting us")
           

        else:
            print("Invalid option selected, please try again")
        
        
    else:
        print("Password incorrect, please try again")


else:

    print("Name not found, please try again")
