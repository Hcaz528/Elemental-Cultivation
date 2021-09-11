import random

"""
VARIABLES
"""
MAX_POWER = 100
Enemy_Types = ["Beast", "Humanoid", "Robot"]

Beast_Enemies = [
    {"Name": "ArticCuno", "HP": 100,
        "Power": 50, "PowerSet": "Set1"},
    {"Name": "Fire Snake", "HP": 100,
        "Power": 50, "PowerSet": "Set2"},
]
Humanoid_Enemies = [
    {"Name": "Lizard Man", "HP": 100,
        "Power": 50, "PowerSet": "Set3"},
    {"Name": "Snake Eater", "HP": 100,
        "Power": 50, "PowerSet": "Set4"},
]
Robot_Enemies = [
    {"Name": "Future Bot", "HP": 100,
        "Power": 50, "PowerSet": "Set5"},
    {"Name": "uRobot Vacuum", "HP": 25,
        "Power": 50, "PowerSet": "Set6"},
]


# Simple choice from available power set
def chooseAction(powerSet):
    return random.choice(powerSet)


# Simple
def setPower():
    return random.randint(0, MAX_POWER)


# Future OOP BOT goes here
