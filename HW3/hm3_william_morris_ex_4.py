"""
Homework 3, Exercise 4
William Morris
2/12/19
This program simulates the inventory of a fantasy game.
"""

inventory = {'Rope': 1,
             'Torch': 6,
             'Gold coin': 42,
             'Dagger': 1,
             'Arrow': 12}

# prints the inventory in a pretty format
def showInventory(inventory):
    print("Item".ljust(12) + "Number of items".ljust(12))
    for k, v in inventory.items():
        print(k.ljust(12) + str(v).ljust(12))

# deletes inventory of the item specified
def delInventoryItem(item, number):
    if item in inventory.keys():
        inventory[item] -= number

# adds item and/or number of items specified to inventory
def addToInventory(item, number):
    if item in inventory.keys():
        inventory[item] += number
    else:
        inventory[item] = number

showInventory(inventory)