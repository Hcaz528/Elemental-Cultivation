from tools_module import checkKeyThenAddOrRemove, checkKeyThenRemove, checkKeyThenAdd, countUniqueTypes, callBackTest
# import inventory_class
print("Item and Inventory System Loaded")


class Item:
    # Class attribute
    amount = 0

    def __init__(self, Name=None, Description=None, Defense=None, Attack=None, Dodge=None, Heal=None, Stamina=None, Uses=1, active=True):
        self.Name = Name if not None else ""
        self.Description = Description if not None else ""
        self.Defense = Defense if not None else 0
        self.Attack = Attack if not None else 0
        self.Dodge = Dodge if not None else 0
        self.Heal = Heal if not None else 0
        self.Stamina = Stamina if not None else 0
        self.Uses = Uses
        self.active = active


# a = Item("Potion", None, None, None, None, None, None, 2, False)
# print(a)
# a.amount += 1
# print(a.amount)
# print(a.Description)

"""
Global Variable
"""
inventory = {}
itemsV0 = {"Potion": {"Name": "Potion", "Description": "It heals me when injuried", "Afffect": 35, "Type": "HP", "Uses": 1},
           "Food": {"Name": "Food", "Description": "", "Afffect": 20, "Type": "HP", "Uses": 1},
           "Coffee": {"Name": "Coffee", "Description": "", "Afffect": 25, "Type": "AP", "Uses": 1},
           "Water": {"Name": "Water", "Description": "", "Afffect": 25, "Type": "AP", "Uses": 1},
           "Sword": {"Name": "Sword", "Description": "", "Afffect": 12, "Type": "Dmg_Out", "Uses": 8},
           "Dagger": {"Name": "Dagger", "Description": "", "Afffect": 6, "Type": ["Dmg_Out", "Shield"], "Uses": 5},
           "Buckler": {"Name": "Buckler", "Description": "", "Afffect": 0.10, "Type": "Shield", "Uses": 5},
           "SewerGrate": {"Name": "Sewer Grate", "Description": "", "Afffect": 0.15, "Type": "Shield", "Uses": 2},
           "EnergySphere": {"Name": "Energy Sphere Grate", "Description": "", "Afffect": 0.15, "Type": "Shield", "Uses": 2},
           }
items = {"Potion": {"Name": "Potion", "Description": "It heals me when injuried", "Defense": 35, "Attack": 10, "Dodge": 10, "Heal": 10, "Stamina": 10, "Uses": 1},
         }

"""
Types of items
"""

TESTING_INVENTORY = False

"""
FUNCTIONS
"""


def displayInventory():
    global inventory
    print("\nYou have the following items in my possession: ")
    for i in inventory.items():
        print(f'{i[0]}: {i[1]}')
    if len(inventory.values()) == 0:
        print("You have nothing in here...")
    print("You've reached the bottom of my bag...\n")


def stealFromInventory(target):
    global inventory
    stolenItem = inventory.pop(target)
    return stolenItem


def pickUp(item, count=0):
    global inventory
    if(count):
        print(f"You picked up {count} {item}s")
        inventory = checkKeyThenAddOrRemove(
            inventory, item, {"removeFlag": False, "quantity": count})
    else:
        print(f"You picked up a {item}")
        inventory = checkKeyThenAddOrRemove(inventory, item)


def drop(item, count=0):
    global inventory
    if(count):
        print(f"You dropped {count} {item}s")
        inventory = checkKeyThenAddOrRemove(
            inventory, item, {"removeFlag": True, "quantity": count})
    else:
        print(f"You dropped one {item}")
        inventory = checkKeyThenAddOrRemove(
            inventory, item,  {"removeFlag": True})
    cleanUpInventory()


def cleanUpInventory():
    global inventory
    # delete = [key for key in myDict if key == 3]
    for i in list(inventory.keys()):
        # print(i, inventory[i])
        if(inventory[i] <= 0):
            del inventory[i]
    # print("done")


def cleanUpInventoryV2():
    global inventory
    # Dictionary Compression ==>
    # k: Key
    # V: Value
    #  {k:v for (k,v) in dict1.items()}
    # This Dictionary Compression makes a list of the keys that we will go over later
    delete = [key for key in inventory if inventory[key] <= 0]
    for key in delete:
        del inventory[key]


"""
TESTING EXAMPLES
"""
if TESTING_INVENTORY:
    # Prop = 1
    inventory = checkKeyThenAddOrRemove(inventory, "Prop")
    print(inventory)

    inventory = checkKeyThenAdd(inventory, "Sword")
    print(inventory)

    inventory = checkKeyThenAddOrRemove(
        inventory, "Potion", {"removeFlag": False, "quantity": 5})
    print(inventory)

    # Prop = 2
    inventory = checkKeyThenAddOrRemove(
        inventory, "Prop", {"removeFlag": False, "quantity": 1})
    print(inventory)

    # Prop = 5
    inventory = checkKeyThenAddOrRemove(
        inventory, "Prop", {"removeFlag": False, "quantity": 3})
    print(inventory)

    # Prop = 4
    inventory = checkKeyThenAddOrRemove(
        inventory, "Prop", {"removeFlag": True})
    print(inventory)

    # Prop = 2
    inventory = checkKeyThenAddOrRemove(
        inventory, "Prop", {"removeFlag": True, "quantity": 2})
    print(inventory)

    # Prop = 0
    inventory = checkKeyThenAddOrRemove(
        inventory, "Prop", {"removeFlag": True, "quantity": 3})
    print(inventory)

    cleanUpInventoryV2()
    print(inventory)
    displayInventory()

"""
1
2
5
4
2
0
"""
