"""
IMPORTS
"""
import random
import math

"""
OBJECT METHOD(Lambda) TOOLS
"""
# Tools Object Methods with lambda functions/ Quick Tools
tools = {
    'version': '0.1',
    'dollarRound': lambda num: round(num*100)/100,
    'percentRound': lambda num: round(num*10000)/100,
    'currencyPrint': lambda currency, num: str(currency)+" "+str(round(num*100)/100),
    # Same as Python's randInt
    'randomNumber': lambda min, max: math.ceil(random.random() * (max-min)+min),
    # 'twoParameterDoubleCallback': lambda callbackA, callbackB, ObjectA, ObjectB: callbackA(ObjectA, ObjectB),
}


def doubleCallback(callback, Object1, Object2):
    return callback(Object1, Object2), callback(Object2, Object1)


def callBackTest(callBack, Object):
    Object = callBack(Object["Object"], Object["Value"])
    print(Object)

# Probably great for adding something to an inventory


def checkKeyThenAddOrRemove(dict, key, options={"removeFlag": False, "quantity": 1}):
    """
    options = { removeFlag, quantity }
    """
    # Check the options dictionary to see if its formatted correctly
    if "quantity" in options.keys() and not("removeFlag" in options.keys()):
        ValueError("Please provide the removeFlag")
        return dict
    if not("quantity" in options.keys()) and "removeFlag" in options.keys():
        options["quantity"] = 1

    if key in dict.keys() and not(options["removeFlag"]):
        # The tenary operator checks that the quantity passed is not less then 0, otherwise it passes a zero
        dict[key] += options["quantity"] if options["quantity"] >= 0 else 0
        return dict
    elif key in dict.keys() and options["removeFlag"]:
        # The tenary operator checks that the quantity passed is less then the dictionary length,
        #  otherwise it passes the len of the dicitonary to take off
        dict[key] -= options["quantity"] if options["quantity"] <= dict[key] else dict[key]
        return dict
    else:
        dict[key] = options["quantity"] if options["quantity"] >= 1 else 1
        return dict

# Probably great for adding something to an inventory
# def checkKeyThenAddOrRemove(dict, key, options={"removeFlag": False, "quantity": 1}):
#     """
#     options = { removeFlag, quantity }
#     """
#     if key in dict.keys() and not(options["removeFlag"]):
#         dict[key] += 1
#         return dict
#     elif key in dict.keys() and options["removeFlag"]:
#         dict[key] -= 1
#         return dict
#     else:
#         dict[key] = 1
#         return dict


# Great for looping over a List to count certain things
def checkKeyThenAdd(dict, key):
    if key in dict.keys():
        dict[key] += 1
        return dict
    else:
        dict[key] = 1
        return dict


def checkKeyThenRemove(dict, key):
    if key in dict.keys():
        dict[key] -= 1 if dict[key] >= 1 else 0
        return dict
    else:
        return dict

# Probably great for adding something to an inventory


def countUniqueTypes(resultDict, list):
    def innerCheckKeyThenAdd(dict, key):
        if key in dict.keys():
            dict[key] += 1
            return dict
        else:
            dict[key] = 1
            return dict

    for i in list:
        resultDict = innerCheckKeyThenAdd(resultDict, i)

    return resultDict


def factorial(num):
    # Basically num! where if 5! then it is 5*4*3*2*1 = 120
    if num == 1:
        return num
    else:
        return num*factorial(num-1)


# def debugPoints(obj, num):
#     print("Debug Point", num, "====START====")
#     print(PlayerX)
#     # print(PlayerX["Advantage"])
#     print(PlayerY)
#     print(type(PlayerY))
#     print(PlayerY["Power"])
#     print("Debug Point", num, "====END====")
