# Dictionaries is a way of storing values and a collection of items.
# a dictionary helps you get a value for a key


first_variable = {}
second_variable = dict()

#print(type(first_variable))


fruit_basket = {
    "mangoes": 40, 
    "oranges": {"bad": 20, "good": 40}, 
    "pawpaw": 10
    }

import copy

new_fruit_basket = copy.deepcopy(fruit_basket)

print("New_Fruit_Basket:", new_fruit_basket)

print("Fruit_Basket:", fruit_basket)

fruit_basket["oranges"]["bad"] = 20

print("New_Fruit_Basket:",new_fruit_basket)

#print("original fruit_basket:", fruit_basket)
# print(len(first_variable))
# print(len(fruit_basket))
# print(isinstance(fruit_basket, list))

mangoes = fruit_basket["mangoes"]

#print("We have {} mangoes".format(mangoes))

mangoes = fruit_basket.get("apples", 0)

all_fruit_keys = fruit_basket.keys()

# print(all_fruit_keys)

# fruit_basket.update({"apples": 100})

# print(fruit_basket)

# print(fruit_basket.items())

# new_fruit_basket = fruit_basket["mangoes"]-1

# print(new_fruit_basket)

# fruit_basket["mangoes"] = fruit_basket["mangoes"]-1

# print(fruit_basket)


# conditionals
# #if statement

# if "mangoes" in fruit_basket:
#     print(True)

#pop items

#fruit_basket.pop("mangoes")
#print(fruit_basket)

#clear




