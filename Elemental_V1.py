""" IMPORTS """
from tools_module import tools, doubleCallback
from game_pkg import battleSystem, player, path_writer

"""
VARAIBLES
"""
roundNum = 1
StartFightSimulation = False
gameOn = True
"""
FUNTIONS
"""


def ExitGame(diedFlag=False, final_score=0):
    print("\nYou succumbed to your wounds..." if diedFlag else "\n")
    print(f'Your final Cultivation score was {final_score}')
    print(f'Thanks for playing!')
    exit()


def main_menu(name):
    print("")
    print(f"""         === Main Menu ===
                        Welcome {name},
            Please pick an option from below to continue...
            ------------------------------------------
            | 1.    New Game   |   2.    Load Game    |
            ------------------------------------------
            ------------------------------------------
            | 3.    Exit       |                      |
            ------------------------------------------""")


def title(which=0):
    if which == 0:
        # Slant Relief
        print("""
__/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\__________________________________________________________________________________________________/\\\\\\\\\\\\____
 _\\/\\\\\\///////////__\\////\\\\\\_________________________________________________________________________________________________\\////\\\\\\____
  _\\/\\\\\\________________\\/\\\\\\________________________________________________________________________/\\\\\\________________________\\/\\\\\\____
   _\\/\\\\\\\\\\\\\\\\\\\\\\________\\/\\\\\\________/\\\\\\\\\\\\\\\\_____/\\\\\\\\\\__/\\\\\\\\\\_______/\\\\\\\\\\\\\\\\___/\\\\/\\\\\\\\\\\\____/\\\\\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\\\\_______\\/\\\\\\____
    _\\/\\\\\\///////_________\\/\\\\\\______/\\\\\\/////\\\\\\__/\\\\\\///\\\\\\\\\\///\\\\\\___/\\\\\\/////\\\\\\_\\/\\\\\\////\\\\\\__\\////\\\\\\////__\\////////\\\\\\______\\/\\\\\\____
     _\\/\\\\\\________________\\/\\\\\\_____/\\\\\\\\\\\\\\\\\\\\\\__\\/\\\\\\_\\//\\\\\\__\\/\\\\\\__/\\\\\\\\\\\\\\\\\\\\\\__\\/\\\\\\__\\//\\\\\\____\\/\\\\\\________/\\\\\\\\\\\\\\\\\\\\_____\\/\\\\\\____
      _\\/\\\\\\________________\\/\\\\\\____\\//\\\\///////___\\/\\\\\\__\\/\\\\\\__\\/\\\\\\_\\//\\\\///////___\\/\\\\\\___\\/\\\\\\____\\/\\\\\\_/\\\\___/\\\\\\/////\\\\\\_____\\/\\\\\\____
       _\\/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\\\\__\\//\\\\\\\\\\\\\\\\\\\\_\\/\\\\\\__\\/\\\\\\__\\/\\\\\\__\\//\\\\\\\\\\\\\\\\\\\\_\\/\\\\\\___\\/\\\\\\____\\//\\\\\\\\\\___\\//\\\\\\\\\\\\\\\\/\\\\__/\\\\\\\\\\\\\\\\\\_
        _\\///////////////__\\/////////____\\//////////__\\///___\\///___\\///____\\//////////__\\///____\\///______\\/////_____\\////////\\//__\\/////////__
        """)
    elif which == 1:
        print("""
      ___           ___       ___           ___           ___           ___           ___           ___           ___
     /\\  \\         /\\__\\     /\\  \\         /\\__\\         /\\  \\         /\\__\\         /\\  \\         /\\  \\         /\\__\\
    /::\\  \\       /:/  /    /::\\  \\       /::|  |       /::\\  \\       /::|  |        \\:\\  \\       /::\\  \\       /:/  /
   /:/\\:\\  \\     /:/  /    /:/\\:\\  \\     /:|:|  |      /:/\\:\\  \\     /:|:|  |         \\:\\  \\     /:/\\:\\  \\     /:/  /
  /::\\~\\:\\  \\   /:/  /    /::\\~\\:\\  \\   /:/|:|__|__   /::\\~\\:\\  \\   /:/|:|  |__       /::\\  \\   /::\\~\\:\\  \\   /:/  /
 /:/\\:\\ \\:\\__\\ /:/__/    /:/\\:\\ \\:\\__\\ /:/ |::::\\__\\ /:/\\:\\ \\:\\__\\ /:/ |:| /\\__\\     /:/\\:\\__\\ /:/\\:\\ \\:\\__\\ /:/__/
 \\:\\~\\:\\ \\/__/ \\:\\  \\    \\:\\~\\:\\ \\/__/ \\/__/~~/:/  / \\:\\~\\:\\ \\/__/ \\/__|:|/:/  /    /:/  \\/__/ \\/__\\:\\/:/  / \\:\\  \\
  \\:\\ \\:\\__\\    \\:\\  \\    \\:\\ \\:\\__\\         /:/  /   \\:\\ \\:\\__\\       |:/:/  /    /:/  /           \\::/  /   \\:\\  \\
   \\:\\ \\/__/     \\:\\  \\    \\:\\ \\/__/        /:/  /     \\:\\ \\/__/       |::/  /     \\/__/            /:/  /     \\:\\  \\
    \\:\\__\\        \\:\\__\\    \\:\\__\\         /:/  /       \\:\\__\\         /:/  /                      /:/  /       \\:\\__\\
     \\/__/         \\/__/     \\/__/         \\/__/         \\/__/         \\/__/                       \\/__/         \\/__/
""")
    else:
        # Graffiti
        print("""
    ___________.__                                __         .__
    \\_   _____/|  |   ____   _____   ____   _____/  |______  |  |
    |    __)_ |  | _/ __ \\ /     \\_/ __ \\ /    \\   __\\__  \\ |  |
    |        \\|  |_\\  ___/|  Y Y  \\  ___/|   |  \\  |  / __ \\|  |__
    /_______  /|____/\\___  >__|_|  /\\___  >___|  /__| (____  /____/
            \\/           \\/      \\/     \\/     \\/          \\/
        """)


def unpackElements(a, b, c):
    elements = [{'1': "Fire"}, {'2': "Lightning"}, {
        '3': "Wind"}, {"4": "Water"}, {'5': "Earth"}]
    # print(dict(elements[a], **elements[b], **elements[c]))
    return dict(elements[a], **elements[b], **elements[c])


chosen_set = {}
PowerSet = {"Set1": {"Name": "Chilled Embers",
                     "Powers": unpackElements(2, 3, 0)},  # ["Wind", "Water", "Fire"]
            "Set2": {"Name": "Fel Touched",
                     "Powers": unpackElements(0, 4, 1)},  # ["Fire", "Earth", "Lightning"]
            "Set3": {"Name": "Storm",
                     "Powers": unpackElements(1, 2, 3)},  # ["Lightning", "Wind", "Water"]
            "Set4": {"Name": "Classic",
                     "Powers": unpackElements(3, 0, 4)},  # ["Water", "Fire", "Earth"]
            "Set5": {"Name": "Nature",
                     "Powers": unpackElements(4, 1, 2)},  # ["Earth", "Lightning", "Wind"]
            "Set6": {"Name": "The Band",
                     "Powers": unpackElements(4, 2, 0)}}  # ["Earth", "Wind", "Fire"]

# >>> {"pong": { "red": 52} , **{"blue":24}}
"""
INVOCATION
"""

# {
#             '1': "Fire",
#             '2': "Lightning",
#             '3': "Wind",
#             '4': "Water",
#             '5': "Earth",
#         }

Main_Player = {"Name": None, "Inventory": {}, "Power": 100, "Max_Power": 100, "HP": 100, "Elemental_Set": {'1': "Fire", '2': "Lightning",
                                                                                                           '3': "Wind"}}

PlayerA = {"Name": "Jason", "HP": 100,
           "Element": "Fire", "Power": 84, "Max_Power": 100, "Elemental_Set": unpackElements(0, 1, 2)}
PlayerB = {"Name": "Billy", "HP": 100,
           "Element": "Water", "Power": 78, "Max_Power": 100, "Elemental_Set": unpackElements(0, 1, 3)}
PlayerC = {"Name": "Mandy", "HP": 100,
           "Element": "Wind", "Power": 37, "Max_Power": 100, "Elemental_Set": unpackElements(0, 3, 4)}
PlayerD = {"Name": "Tobe", "HP": 100,
           "Element": "Lightning", "Power": 56, "Max_Power": 100, "Elemental_Set": unpackElements(1, 3, 4)}
PlayerE = {"Name": "Caprice", "HP": 100,
           "Element": "Earth", "Power": 25, "Max_Power": 100, "Elemental_Set": unpackElements(0, 2, 4)}

# NOTE Fully integrate the battling system to the Monster, MiniBoss, and Boss points


if StartFightSimulation:
    PlayerA, PlayerB = battleSystem.fight(PlayerA, PlayerB)
else:
    print("Welcome to...")
    title()
    name = input("What would you like your name to be? ")
    # title(1)
    # input()
    # print("PlayerA's Elemental Set: ",
    #       battleSystem.checkElementalSet(PlayerA["Elemental_Set"]))
    # print(battleSystem.withinSet("Fire", PlayerA["Elemental_Set"]))
    # print(battleSystem.withinSet("Earth", PlayerA["Elemental_Set"]))
    # print(inventory.displayInventory())
    # inventory.pickUp("Sword")
    # inventory.pickUp("Potion", 3)
    # print(inventory.displayInventory())
    # inventory.drop("Potion", 2)
    # inventory.drop("Sword")
    # print(inventory.displayInventory())

    while gameOn:
        main_menu(name)
        option = input("Pick an option: ")

        if option.isdigit() and int(option) not in [1, 2, 3]:
            print("Please pick a valid selection")
        elif option == "1":
            print("New Game Selected")

            while True:
                print(
                    f'\nSo {name} you have chosen your name, now you must choose your Elemental power set')
                print(f'You may be wondering what is a Elemental Power Set')
                print(f'You may be wondering what type of game this is...')
                print(
                    f'To answer those questions briefly this game is a text based adventure')
                print(
                    f'You can chose your actions and at times you will have to defend yourself')
                print(
                    f'In those cases you would have to fight, but it is not normal fisticuffs')
                print(
                    f'No disputes are handled by the magical game of Elemental Jan Ken Po')
                print(
                    "In other words its like Rock-Paper-Scissors-Spock-Lizard, except with the 5 elements")
                print(
                    "Control Lightning, blast Fire, mold Earth, direct Wind, and command Water")
                print("\nWith all that said, why don't you pick your Elemental suite:\n")
                i = 1
                for key, items in PowerSet.items():
                    string_print = f'{i}. POWER SET: {items["Name"]}\t\tElements:\t'
                    for x in items["Powers"].items():
                        string_print += f'{x[1]} '
                    print(string_print+'\n')
                    i += 1
                option = input(
                    "Which suite of elements would you prefer to command? ")

                if option.isdigit() and int(option) not in range(1, 7):
                    print("\nYou must choose a valid selection.")
                else:
                    chosen_set = PowerSet[f"Set{option}"]['Powers']
                    break
                print(chosen_set)
            player_one = player.Player(name, {}, 100, 100, 100, chosen_set)
            print(
                f"\nCharacter creation for {player_one.Name} has completed...")
            input("Press enter to continue...")
            path_writer.readPathStory(path_writer.writePath(), player_one)
        elif option == "2":
            print("Loading Game from file")
            input("Press enter to continue...")
            player_one = player.Player()
            player_one.fullLoadPersonDict(
                path_writer.loadPlayer('Player_save.json'))

            path_writer.readPathStory(path_writer.writePath(True), player_one)
        elif option == "3":
            print("Exitting Game")
            input("Press enter to continue...")
            ExitGame()

        # gameOn = False

print('END OF GAME')

"""
HIGH LEVEL ALGORITHM

    Walk down path
    Check if there is an event
    If event can you interact with it (battle, action, etc.)
    Conclude event and continue walking down the path
    If Health drops to zero GAME OVER
    If you reach the end of the path and finish the last event you win!
"""
