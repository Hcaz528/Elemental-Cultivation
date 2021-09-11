import math
from tools_module import tools, doubleCallback
from game_pkg import battleSystem, inventory, simpleAI
print("Battle System Loaded")


DEBUG_POWER = 50
DEBUG_ELEMENT = "Fire"
DEBUG = False

"""
VARAIBLES
"""
elements = ["Fire", "Water", "Wind", "Earth", "Lightning"]
subScenario_active = False
main_scenario_active = False
succesiveHit = {"juggleCount": 0, "hitBefore": False}
roundNum = 1

# Power Sets
PowerSet = {"Set1": {"Name": "Chilled Embers",
                     "Powers": ["Wind", "Water", "Fire"]},
            "Set2": {"Name": "Fel Touched",
                     "Powers": ["Fire", "Earth", "Lightning"]},
            "Set3": {"Name": "Storm",
                     "Powers": ["Lightning", "Wind", "Water"]},
            "Set4": {"Name": "Classic",
                     "Powers": ["Water", "Fire", "Earth"]},
            "Set5": {"Name": "Nature",
                     "Powers": ["Earth", "Lightning", "Wind"]},
            "Set6": {"Name": "The Band",
                     "Powers": ["Earth", "Wind", "Fire"]}}


"""
FUNCTIONS
"""


def SwitchCase(Element):
    # Bootleg Switch Case
    # Switch Case is called Match Case and that comes in Python 3.10
    if(Element == "1" or Element == "2" or Element == "3" or Element == "4" or Element == "5"):
        return {
            '1': "Fire",
            '2': "Lightning",
            '3': "Wind",
            '4': "Water",
            '5': "Earth",
        }[Element]
    else:
        return Element


def elementalComparison(PlayerX, PlayerY):
    """
    ## Elemental Comparison Function
    Takes in two player objects and compares the elements chosen both to determine a winner

    ### Expected incoming Player Object = {Name, Element, Power}
    ### Expected outgoing Player Object = {Name, Element, Power, Advantage}
    """

    PlayerX["Element"] = SwitchCase(PlayerX["Element"])
    PlayerY["Element"] = SwitchCase(PlayerY["Element"])
    PlayerA = PlayerX
    PlayerA["Advantage"] = False

    # 1. If user and computer choose the same Element, it is a tie that will need to be broken by the amount of POWER that either has put behind the attack
    if ((PlayerX["Element"]).lower() == (PlayerY["Element"]).lower()):
        return PlayerA  # NOTE remember to always return a dictionary type not a list type
    # 3. If one chose Fire and one chose Wind or Lightning, Fire wins
    elif ((PlayerX["Element"]).lower() == ("Fire").lower()) and ((PlayerY["Element"]).lower() == ("Lightning").lower() or (PlayerY["Element"]).lower() == ("Wind").lower()):
        PlayerA["Advantage"] = True
        return PlayerA
    # 4. If one chose Lightning and one chose Wind or Water, Lightning wins
    elif ((PlayerX["Element"]).lower() == ("Lightning").lower()) and ((PlayerY["Element"]).lower() == ("Water").lower() or (PlayerY["Element"]).lower() == ("Wind").lower()):
        PlayerA["Advantage"] = True
        return PlayerA
    # 6. If one chose Wind and one chose Earth or Water, Wind wins
    elif ((PlayerX["Element"]).lower() == ("Wind").lower()) and ((PlayerY["Element"]).lower() == ("Earth").lower() or (PlayerY["Element"]).lower() == ("Water").lower()):
        PlayerA["Advantage"] = True
        return PlayerA
    # 8. If one chose Water and one chose Earth or Fire, Water wins
    elif ((PlayerX["Element"]).lower() == ("Water").lower()) and ((PlayerY["Element"]).lower() == ("Earth").lower() or (PlayerY["Element"]).lower() == ("Fire").lower()):
        PlayerA["Advantage"] = True
        return PlayerA
    # 10. If one chose Earth and one chose Fire or Lightning, Earth wins
    elif ((PlayerX["Element"]).lower() == ("Earth").lower()) and ((PlayerY["Element"]).lower() == ("Fire").lower() or (PlayerY["Element"]).lower() == ("Lightning").lower()):
        PlayerA["Advantage"] = True
        return PlayerA
    # Expected outgoing Player Object = {Name, Element, Power, Advantage}

    # Note to self I was passing a [] which is a list, with this in mind I got the following error "TypeError: list indices must be integers or slices, not str"
    # I should and am now passing back the PlayerA dictionary
    return PlayerA


def powerComparison(PlayerX, PlayerY):
    """
    ## Power Comparison Function
    Takes in two player objects and compares the power behind the attacks

    ### Expected incoming Player Object = {Name, HP, Element, Power, Advantage}
    ### Expected outgoing Player Object = {Name, HP-Dmaage, Element, Power, Advantage}
    """
    def innerPowerComparison(x, y):
        EXTRA_DAMAGE = 1.80  # 180% # If you win with advantage you do this damage
        REDUCED_DAMAGE = 0.5  # 50% # if you win with disadvantage you do this damage
        # (powerX, powerY, damaged)
        powerDiff = abs(x - y)
        power_range = 5
        if x > y + power_range:
            return math.floor(powerDiff*EXTRA_DAMAGE)
        elif x < y - power_range:
            return math.ceil(REDUCED_DAMAGE*powerDiff)
        elif (x >= (y - power_range)) or (x <= (y + power_range)):
            return powerDiff

    def exchangeHits(PlayerA, PlayerB):
        # print(f'PlayerA["Name"] {PlayerA["Name"]}')
        # print(f'PlayerB["Name"] {PlayerB["Name"]}')

        if PlayerA["Power"] > PlayerB["Power"] + 5:
            dmg = innerPowerComparison(
                PlayerA["Power"], PlayerB["Power"])
            print(
                f'{PlayerA["Name"]} wins the exchange! {dmg} points of damage done to {PlayerB["Name"]}')
            PlayerB["HP"] -= innerPowerComparison(
                PlayerA["Power"], PlayerB["Power"])
        elif PlayerB["Power"] > PlayerA["Power"] + 5:
            dmg = innerPowerComparison(
                PlayerA["Power"], PlayerB["Power"])
            print(
                f'{PlayerB["Name"]} wins the exchange, even with {PlayerA["Name"]} elemental advanatge! {PlayerA["Name"]} takes {dmg} points of damage')
            PlayerA["HP"] -= dmg
        else:
            dmg = innerPowerComparison(
                PlayerA["Power"], PlayerB["Power"])
            print("SIMILAR AMOUNT OF POWER OUTPUT FORM BOTH SIDES!!!")
            print("Looks like they both got SCRATCHED in the scuffle!",
                  dmg, "Points of Damage")
            PlayerB["HP"] -= dmg
            PlayerA["HP"] -= dmg
        return PlayerA, PlayerB

    if PlayerX["Advantage"]:
        PlayerX, PlayerY = exchangeHits(PlayerX, PlayerY)
        return PlayerX, PlayerY
    elif PlayerY["Advantage"]:
        PlayerY, PlayerX = exchangeHits(PlayerY, PlayerX)
        return PlayerX, PlayerY
    # Player Object = {Name, Advantage, Power}
    print("SAME ELEMENT CLASH!!! No damage done to either side")
    return PlayerX, PlayerY


def checkElementalSet(elSet):
    elementalSet = ""
    for x, y in elSet.items():
        elementalSet += f"\n{y}({x})"
    elementalSet += "\n"
    return elementalSet


def withinSet(choice, elSet):
    return choice in elSet.values()


# Main Fight Loop
def fight(PlayerA, PlayerB):
    global roundNum
    # Match Up 1
    print("\nMatch Up 1")

    # Default input
    # PlayerA["Name"] = input("What is your name? ") or PlayerA["Name"]

    print("\nWelcome to the fight", PlayerA["Name"] + "!")

    matchOver = False

    elemental_set_in_use = ''
    elemental_set_in_use_values = []
    n = 0
    for k, v in PlayerA['Elemental_Set'].items():
        elemental_set_in_use += f"\n{v}({k})"
        elemental_set_in_use_values.append(k)
        if n < len(PlayerA['Elemental_Set'].items())-1:
            elemental_set_in_use += f","
        n += 1

    enemy_elements = []
    for k, v in PlayerB['Elemental_Set'].items():
        enemy_elements.append(k)

    # print("You are PlayerA:", PlayerA["Name"], ". Good Luck!")
    while not(matchOver):
        print("\nRound", roundNum, "\n\n")
        print(f'{PlayerA["Name"]}\'s HP {PlayerA["HP"]}')
        print(f'{PlayerB["Name"]}\'s HP {PlayerB["HP"]}\n')
        input("Hit enter to continue the fight...")
        roundNum += 1

        print("\nGet ready for the next barrage of attacks!")
        # print(PlayerA)
        # Ready next round
        while True:
            PlayerA["Power"] = input(
                "How much power behind the attack? (0 - 100): ")
            PlayerA["Element"] = input(
                f"What element are you using?{elemental_set_in_use}: ")
            if PlayerA["Power"].isdigit() and int(PlayerA["Power"]) > 0 and PlayerA["Element"] in elemental_set_in_use_values:
                PlayerA["Power"] = int(PlayerA["Power"])
                break
            print(
                "\nPlease pick a valid selection from the list! ALSO ensure that the power is an int")

        cpuPower = DEBUG_POWER if DEBUG else simpleAI.setPower()
        cpuElement = DEBUG_ELEMENT if DEBUG else simpleAI.chooseAction(
            enemy_elements)

        PlayerB["Power"], PlayerB["Element"] = cpuPower, cpuElement
        print(
            f'\n{PlayerA["Name"]} launched an attack with the element: {SwitchCase(PlayerA["Element"])}\nat power level: {PlayerA["Power"]}')
        print(
            f'\n{PlayerB["Name"]} launched an attack with the element: {SwitchCase(PlayerB["Element"])}\nat power level: {PlayerB["Power"]}')
        # Compare the elments of the combatants and see who has the advantage in the Elemental Janken
        PlayerA, PlayerB = doubleCallback(
            battleSystem.elementalComparison, PlayerA, PlayerB)

        # Compares the power levels of the attacks
        PlayerA, PlayerB = battleSystem.powerComparison(PlayerA, PlayerB)
        # print(PlayerA, "\n", PlayerB)
        print("\nBlows were exchanged!")

        if PlayerA["HP"] <= 0 or PlayerB["HP"] <= 0:
            if PlayerA["HP"] <= 0:
                print(PlayerB["Name"], "Wins!~\n")
            else:
                print(PlayerA["Name"], "Wins!~\n")
            matchOver = True
            roundNum = 1
            break

    return PlayerA, PlayerB
