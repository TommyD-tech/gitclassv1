class Budget:

    def __init__(self,category):
        self.category = category
        self.amount = 0

    def check_balance(self,amount):
        if self.amount < amount:
            return False
        else:
            return True
    
    def deposit(self, amount):
        self.amount += amount
        return "You deposited {} into the budget".format(amount)

    def withdraw(self, amount):
        if self.check_balance(amount) == True:
            self.amount -= amount
            return "You withdrew {} from the budget".format(amount)
        else:
            return "You do not have sufficient balance to perform this operation"

    def budget_balance(self):
        return self.amount

    def transfer(self, amount, category):
        if self.check_balance(amount) == True:
            self.amount -= amount
            return "You have transfered {} to {}".format(amount, category.category)
        else:
            return "You do not have enough balance to perform this transfer"

# Deposit operations
food = Budget("food")
food.deposit(1000)
print("food.deposit: #{}".format(food.budget_balance()))

clothing = Budget("clothing")
clothing.deposit(2000)
print("clothing.deposit: #{}".format(clothing.budget_balance()))

entertainment = Budget("entertainment")
entertainment.deposit(3000)
print("entertainment.deposit: #{}".format(entertainment.budget_balance()))

# Withdrawal operations
food.withdraw(500)
print("Food budget balance: #{} after performing withdrawal".format(food.budget_balance()))

clothing.withdraw(350)
print("Clothing budget balance:#{} after performing withdrawal".format(clothing.budget_balance()))

entertainment.withdraw(1000)
print("entertainment budget balance:#{} after performing withdrawal".format(entertainment.budget_balance()))
    
# Transfer Operations
print(food.transfer(200, clothing))
print("Food budget balance: #{} and Clothing budget balance: #{} after performing transfer".format(food.budget_balance(), clothing.budget_balance()))    


print(clothing.transfer(500, entertainment))
print("Clothing budget balance: #{} and Entertainment budget balance: #{} after performing transfer".format(clothing.budget_balance(), entertainment.budget_balance()))