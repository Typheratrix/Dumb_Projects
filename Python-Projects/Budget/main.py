import budget
from budget import create_spend_chart
from unittest import main

item = input(" What would you like to choose:\n [1]: Food\n [2]: Clothing\n [3]: Auto\n")
method = input("Would you like to deposit[1] or withdraw [2]: ")
amount = int(input("How much would you like to deposit/withdraw: "))
description = input("What is this for: ")


food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(150)

if item == '1':
    if method == '1':
        food.deposit(amount, description)
    if method == '2':
        food.withdraw(amount, description)
if item == '2':
    if method == '1':
        food.deposit(amount, description)
    if method == '2':
        food.withdraw(amount, description)
if item == '3':
    if method == '1':
        food.deposit(amount, description)
    if method == '2':
        food.withdraw(amount, description)

print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))

# Run unit test automatically
main(module='test_module', exit=False)