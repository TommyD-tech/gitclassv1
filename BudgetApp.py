# To whom it may concern, I didnt get how to generate the balance, I tried watching several videos, i still couldnt understand this classes and objects, hence the lack of excellence in this Budget App
# I would like to appeal to any mentor that will be grading this to please give a comment on how to get better, or give a correction to the entire class on this Classes and object.

class Budget:

    def __init__ (self, category, amount):
        self.category = category
        self.amount = amount

    def withdraw(self):
        selectedoption = int(input("Select amount to withdraw \n (1) 1000 (2) 5000 (3) 50000"))

        if selectedoption == 1:
            print("Succesful Transaction")
        elif selectedoption == 2:
            print("Successful Transaction")
        elif selectedoption == 3:
            print("Insuffient Balance")
        else:
            print("Invalid option selected")

    def deposit(self):
        selectedoption = int(input("Select amount to deposit \n (1) 1000 (2) 5000 (3) 50000"))
        if selectedoption == 1:
            print("Succesful Transaction")
        elif selectedoption == 2:
            print("Successful Transaction")
        elif selectedoption == 3:
            print("Balance is 80000")
        else:
            print("Invalid option selected")

    def transfer_between_categories(self):

        catg = input("What category would you like to transfer from? \n (1) Food (2) Clothing (3) Entertainment \n")
        
        print("How much would you like to transfer")
        print("1. 2000")  
        print("2. 5000")
        print("3. 1000")   



budget_1 = Budget("Food", 10000)
budget_2 = Budget("Clothing", 20000)
budget_3 = Budget("Entertainment", 20000)

print(budget_1.transfer_between_categories())
        

