import random
import json
# from './data_structures' import LinkedList, DoubleLinkedList
# pylint: disable=import-error
from game_pkg.player import Player
from game_pkg.data_structures import LinkedList, DoubleLinkedList, Stack, Queue
from game_pkg.battleSystem import fight
# pylint: enable=import-error
"""
I - Intro
Mi - Mini Boss
B - Boss
Ex - Exposition Point
M - Monster
E - Extra
    S1 - Scenario: Help Someone with one task
    S2 - Explore/Adventure
    S3 - Get an item/skill
"""
pathSTORIES = {}
loadFlag = 0
written_path = ''
conitnue_dialogue = ["You dust yourself off and continue on...\n",
                     "You breathe in the air around you and start walking down the path..."]
DEBUG_FLAG = False  # Turned on when debugging inside the game_pkg
player_Obj = None


def ExitGame(diedFlag=False, final_score=0, saving=False):
    print("\nYou succumbed to your wounds..." if diedFlag else "\n")
    if not(saving):
        print(f'Your final Cultivation score was {final_score}')
        print(f'Thanks for playing!')
    else:
        print("Game is saved...\nGoodbye!")
    exit()


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


def EndGame(final_score):
    print("\n\nWow... a mere low-born like you was able to not only win the tournament but destroy a god's army and end that same god's life.\nBut this means more then the sweet feelings that ripple through you after you avenged the death of your friend Bosman.\nThis sets a new precedent, a turning point in the oppresive histroy fo the gods and the low-borns.\nYour cultivation led you to becoming the first High-born!")
    print(f"\n\nThanks for playing!\nYour final score is {final_score}")
    input("Enter to continue...")
    title()
    exit()


def shuffleStoreis():
    global pathSTORIES
    # random.shuffle(pathSTORIES["Exposition"]) # Why would I want to shuffle the exposition?
    random.shuffle(pathSTORIES["Monster"])
    random.shuffle(pathSTORIES["Scenario-1"]["Scenarios"])
    random.shuffle(pathSTORIES["Scenario-2"]["Scenarios"])
    random.shuffle(pathSTORIES["Scenario-3"]["Scenarios"])


def loadStories(location='game_pkg/paths.json'):
    if DEBUG_FLAG:
        location = "paths.json"

    JSONContents = ''
    with open(location) as f:
        # It reads it and then loads the json
        JSONContents = json.loads(f.read())
    return JSONContents  # Returns JSON as dictionary


def loadPlayer(location='game_pkg/Player_save.json'):
    if DEBUG_FLAG:
        location = "paths.json"

    JSONContents = ''
    with open(location) as f:
        # It reads it and then loads the json
        JSONContents = json.loads(f.read())
    return JSONContents  # Returns JSON as dictionary


def saveStory():
    global pathSTORIES, written_path
    pathSTORIES['written_path'] = written_path
    contents_json = json.dumps(pathSTORIES, indent=4)
    f = open("paths_update.json", "w")
    f.write(contents_json)
    f.close()


def savePlayer(playerObj):
    contents_json = json.dumps(playerObj.returnPersonDict(), indent=4)
    f = open("Player_save.json", "w")
    f.write(contents_json)
    f.close()


def returnPathStore():
    global pathSTORIES
    return pathSTORIES


def pathActionTemplate(pos, actions, story):
    spacer = "              "
    returnText = f"""
              =====================================
              === You are at Mile Marker: {pos} ===
              =====================================

{story}

              You could do the following:
"""
    # NOTE Try to do for i in range(len(actions))
    # Then i would be actions[i]
    n = 1
    choicesObj = []
    for i in actions:
        returnText += f'{spacer}{n}. {i}\n'
        n += 1
        choicesObj.append(i)
    returnText += f"{spacer}or Save(s) to save and quit\n"
    returnText += f"{spacer}or Person(p) to view your stats\n"
    returnText += f"{spacer}What would you like to do? "

    # returns the output
    return returnText, [x for x in range(n+1)][1:n+1], choicesObj


path_chance = ["s1"]


def readPath(pathStr, pathPosition):
    """
    INPUT: X-X-X-X, pathPosition
    OUTPUT: X: Scenario, pathPosition
    """
    pathSplit = pathStr.split('-')

    # print(pathSplit)
    # print(pathSplit[pathPosition-1])

    return pathSplit[pathPosition-1], pathPosition


def writePath(load=False, pathLength=20):
    """"
    Makes a Path string for you
    OUTPUT: X-X-X-X
    """
    global pathSTORIES
    pathString = "I-"
    if not(load):
        # Load Stories
        pathLoc = "game_pkg/paths.json"
        if DEBUG_FLAG:
            pathLoc = "paths.json"
        pathSTORIES = loadStories(pathLoc)

        Exposition_Points = [1, 3, 8, 11, 18]
        Monster_Points = [2, 7, 10, 14]
        MiniBoss_Points = [9]
        Boss_Points = [19]
        E_Points = ["S1", "S1", "S2", "S2", "S2",
                    "S3", "S3", "S3"]  # 8 points in here
        E_Points_Original = list(E_Points)
        # Lesson learned, in Python when putting an list into another list what happens seems to be just passing the reference not making a copy of the list.

        for i in range(pathLength):
            if i in Exposition_Points:
                # print("Exposition point reached", i)
                pathString += "Ex"
            elif i in Monster_Points:
                # print("Monster point reached", i)
                pathString += "M"
            elif i in MiniBoss_Points:
                # print("MiniBoss point reached", i)
                pathString += "Mi"
            elif i in Boss_Points:
                # print("Boss point reached", i)
                pathString += "B"
            else:
                # pathString += "E"
                random.shuffle(E_Points)
                pathString += E_Points.pop()
                if not(E_Points):
                    E_Points = E_Points_Original

            if not(i == pathLength-1):
                pathString += "-"
        """
        I - Intro
        Mi - Mini Boss
        B - Boss
        Ex - Exposition Point
        M - Monster
        E - Extra
            S1 - Scenario: Help Someone with one task
            S2 - Explore/Adventure
            S3 - Get an item/skill
        """
        shuffleStoreis()
    else:
        pathSTORIES = loadStories("paths_update.json")
        pathString = pathSTORIES['written_path']

    return pathString


def action_continue():
    print("You are in continue")


def action_intro(choice, player_Obj=None):
    if(choice == 1):
        print(pathSTORIES["Introduction"]["Uniques"]["Continue"])
        player_Obj.Cultivation += pathSTORIES["Introduction"]["Uniques"]["Cultivation"]
        print(f'Cultivation Score: {player_Obj.Cultivation}')
        input("Press enter to continue...")

    elif(choice == 2):
        print(pathSTORIES["Introduction"]["Uniques"]["Run Away"])
        ExitGame(False, player_Obj.Cultivation, False)


def action_exposition(choice, expObj, player_Obj=None):
    print(f"Hey {player_Obj.Name}")
    print(expObj['Uniques']["Additional_Story"][0])
    if player_Obj.Cultivation >= expObj["Uniques"]['Cultivation']:
        print(expObj['Uniques']["Additional_Story"][1])
        print("Your cultivation score was high enough to impress your friend")
        print("He helped you open your chakras, increasing your vitality...")
        player_Obj.Max_HP += expObj['Uniques']['Reward']['Max_HP']
        print(
            f"Max Health is now {player_Obj.Max_HP} and you have been healed")
        player_Obj.Current_HP = player_Obj.Max_HP
    else:
        print(expObj['Uniques']["Additional_Story"][2])
        print(f"Your friend healed you and then went on his way...")
        player_Obj.Current_HP = player_Obj.Max_HP

    player_Obj.Cultivation += expObj['Uniques']["Cultivation"]
    print(f'Cultivation Score: {player_Obj.Cultivation}')
    input("Press enter to continue...")

    # NOTE You could put something here that would read additional stories for you with an input that pauses it and you hit enter to continue reading


def action_help(choice, choicObj, expObj, player_Obj=None):
    if DEBUG_FLAG:
        print("You are in a help or get item task")

    if(choice == 1):
        print(expObj["Uniques"][choicObj[0]])
        print("\nYou earned some Cultivation going through this action")
        player_Obj.Cultivation += expObj["Uniques"]["Cultivation"]

    elif(choice == 2):
        print(expObj["Uniques"]["Continue On"])
    input("Press enter to continue...")


def action_fight(choice, targetStory, choicObj=None, expObj=None, player_Obj=None):
    if DEBUG_FLAG:
        print("You are in a fight")
        print("You will be facing a", targetStory)
        input("Press enter to continue...")
    if targetStory == "Monster":
        if(choice == 1):  # FIGHT
            print(expObj["Uniques"][choicObj[0]])
            # NOTE Implement BattleSystem Here
            PlayerA = player_Obj.returnPersonDict()
            easyShift = expObj["Uniques"]
            enemy_player = Player(
                easyShift["Name"], {}, 100, 100, easyShift["HP"], easyShift["Elemental_Set"])
            PlayerB = enemy_player.returnPersonDict()
            PlayerA, PlayerB = fight(PlayerA, PlayerB)
            # NOTE What is the result of the battle
            if PlayerA["HP"] <= 0:
                print("You got roughed up pretty bad during the battle...")
                ExitGame(True, player_Obj.Cultivation, False)
            # NOTE Check to see if the player died
            player_Obj.Current_HP = PlayerA["HP"]
            player_Obj.Cultivation = expObj["Uniques"]["Cultivation"]
            print(
                f"\nYou won the battle albeit with a few scraps (current HP {player_Obj.Current_HP})")
            # NOTE If dead ExitGame(True, player_Obj.Cultivation, False)

        elif(choice == 2):
            print(expObj["Uniques"]["Give_Up"])
            print("You lost some Cultivation through running from this fight")
            print("Be careful, you can't always run away...")
            player_Obj.Cultivation -= expObj["Uniques"]["Cultivation"] // 2
            print("Current Cultivation score", player_Obj.Cultivation)
    elif targetStory == "miniBoss":
        if(choice == 1):  # FIGHT
            print(pathSTORIES["miniBoss"]["Uniques"]["Fight!"])
            # NOTE Implement BattleSystem Here
            PlayerA = player_Obj.returnPersonDict()
            easyShift = pathSTORIES["miniBoss"]["Uniques"]
            enemy_player = Player(
                easyShift["Name"], {}, 100, 100, easyShift["HP"], easyShift["Elemental_Set"])
            PlayerB = enemy_player.returnPersonDict()
            PlayerA, PlayerB = fight(PlayerA, PlayerB)
            # NOTE What is the result of the battle
            if PlayerA["HP"] <= 0:
                print("You got roughed up pretty bad during the battle...")
                ExitGame(True, player_Obj.Cultivation, False)
            # NOTE Check to see if the player died
            print(
                f"\nYou won the battle albeit with a few scraps (current HP {player_Obj.Current_HP})")
            player_Obj.Current_HP = PlayerA["HP"]
            player_Obj.Cultivation = pathSTORIES["miniBoss"]["Uniques"]["Cultivation"]
            # NOTE If dead ExitGame(True, player_Obj.Cultivation, False)
        elif(choice == 2):
            print(pathSTORIES["miniBoss"]["Uniques"]["Give_Up"])

            ExitGame(True, player_Obj.Cultivation, False)
    elif targetStory == "Boss":
        if(choice == 1):  # FIGHT
            print(pathSTORIES["Boss"]["Uniques"]["Fight!"])
            # NOTE Implement BattleSystem Here
            PlayerA = player_Obj.returnPersonDict()
            easyShift = pathSTORIES["Boss"]["Uniques"]
            enemy_player = Player(
                easyShift["Name"], {}, 100, 100, easyShift["HP"], easyShift["Elemental_Set"])
            PlayerB = enemy_player.returnPersonDict()
            PlayerA, PlayerB = fight(PlayerA, PlayerB)
            # NOTE What is the result of the battle
            if PlayerA["HP"] <= 0:
                print("You got roughed up pretty bad during the battle...")
                ExitGame(True, player_Obj.Cultivation, False)
            # NOTE Check to see if the player died
            print(
                f"\nYou won the battle albeit with a few scraps (current HP {player_Obj.Current_HP})")
            player_Obj.Current_HP = PlayerA["HP"]
            player_Obj.Cultivation = pathSTORIES["Boss"]["Uniques"]["Cultivation"]
            # NOTE If dead ExitGame(True, player_Obj.Cultivation, False)
            EndGame(player_Obj.Cultivation)
        elif(choice == 2):
            print(pathSTORIES["Boss"]["Uniques"]["Give_Up"])

            ExitGame(True, player_Obj.Cultivation, False)


def action_explore(choice, choicObj, expObj, player_Obj=None):
    if DEBUG_FLAG:
        print("You are in explore")

    if(choice == 1):
        print(expObj["Uniques"][choicObj[0]])
        print("You earned some Cultivation through from that experience")
        player_Obj.Cultivation += expObj["Uniques"]["Cultivation"]
        print("Current Cultivation score", player_Obj.Cultivation)
    elif(choice == 2):
        print(expObj["Uniques"]["Continue On"])
    input("Press enter to continue...")


def returningCorrectStory(Name, ID, Scenario=None):
    if Scenario is not None:
        return [x for x in pathSTORIES[Name]["Scenarios"] if x["Uniques"]["ID"] == ID]
    return [x for x in pathSTORIES[Name] if x["Uniques"]["ID"] == ID]


def evaluate_story_choice(choice, ID, targetStory, choicObj=None, player_Obj=None):
    # print(f'ID, targetStory: {ID, targetStory}')
    exp = []

    if targetStory == "Monster":
        exp = returningCorrectStory("Monster", ID)
    elif targetStory == "Exposition":
        exp = returningCorrectStory("Exposition", ID)
    # elif targetStory == "miniBoss":
    #     exp = returningCorrectStory("miniBoss", ID)
    # elif targetStory == "Boss":
    #     exp = returningCorrectStory("Boss", ID)
    elif targetStory == "Scenario-1":
        exp = returningCorrectStory("Scenario-1", ID, 1)
    elif targetStory == "Scenario-2":
        exp = returningCorrectStory("Scenario-2", ID, 1)
    elif targetStory == "Scenario-3":
        exp = returningCorrectStory("Scenario-3", ID, 1)

    # print(exp)
    # print("What is the targetStory:", targetStory)

    if(pathSTORIES["Introduction"]["Uniques"]["ID"] == ID):
        action_intro(choice, player_Obj)
    elif(targetStory == "Exposition" and exp[0]["Uniques"]["ID"] == ID):
        action_exposition(choice, exp[0], player_Obj)
    elif(targetStory == "Monster" and exp[0]["Uniques"]["ID"] == ID):
        action_fight(choice, targetStory, choicObj, exp[0], player_Obj)
    elif(targetStory == "miniBoss"):
        action_fight(choice, targetStory, None, None, player_Obj)
    elif(targetStory == "Boss"):
        action_fight(choice, targetStory, None, None, player_Obj)
    elif(targetStory == "Scenario-1" and exp[0]["Uniques"]["ID"] == ID):
        action_help(choice, choicObj, exp[0], player_Obj)
    elif(targetStory == "Scenario-2" and exp[0]["Uniques"]["ID"] == ID):
        action_explore(choice, choicObj, exp[0], player_Obj)
    elif(targetStory == "Scenario-3" and exp[0]["Uniques"]["ID"] == ID):
        action_help(choice, choicObj, exp[0], player_Obj)


def evaulate_action(story_bit, choice_array, ID, targetStory=None, choicObj=None, player_Obj=None):

    while True:
        # print("targetStory:", targetStory)
        action = input(story_bit)

        if action.isdigit():
            action = int(action)
        choice_array.append("s")
        choice_array.append("p")

        # Check if the value entered was valid
        if action in choice_array:
            if action == 's':
                saveStory()
                savePlayer(player_Obj)
                print("\n\nGame Saved\nQuitting to Desktop...")
                input("Good bye! (Press enter to exit)")
                ExitGame(False, 0, True)
                return
            elif action == 1:
                if DEBUG_FLAG:
                    print("Action 1")
                # print("Next to Action 1, what is the targetStory", targetStory)
                evaluate_story_choice(
                    action, ID, targetStory, choicObj, player_Obj)
                return
            elif action == 2:
                if DEBUG_FLAG:
                    print("Action 2")
                evaluate_story_choice(
                    action, ID, targetStory, choicObj, player_Obj)
                return
            elif action == 3:
                if DEBUG_FLAG:
                    print("Action 3")
                evaluate_story_choice(
                    action, ID, targetStory, choicObj, player_Obj)
                return
            elif action.lower() == 'p':
                for key, val in player_Obj.returnPersonDict().items():
                    print(f'{key}: -={val}=-')

        print(f'\n\nChoice {action} was not a valid choice\nPlease try again' if not(
            action.lower() == 'p') else "\n\nShowing Stats Profile Window")
    return


def readPathStory(story, player_Obj=None):
    global written_path
    # print(story)
    written_path = story
    position = pathSTORIES["storyPosition"]
    expositionPosition = pathSTORIES["expositionPosition"]
    monsterPosition = pathSTORIES["monsterPosition"]
    scenarioOnePosition = pathSTORIES["scenarioOnePosition"]
    scenarioTwoPosition = pathSTORIES["scenarioTwoPosition"]
    scenarioThreePosition = pathSTORIES["scenarioThreePosition"]
    action = ""
    length = len(story.split('-'))
    while position <= length:
        story_chunk = readPath(story, position)
        # print("story_chunk:", story_chunk)
        # Introduction
        if story_chunk[0] == "I":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["Introduction"]["Actions"], pathSTORIES["Introduction"]["Story"])

            evaulate_action(story_bit, choice_array,
                            pathSTORIES["Introduction"]["Uniques"]["ID"], None, None, player_Obj)

        # Exposition
        elif story_chunk[0] == "Ex":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["Exposition"][expositionPosition]["Actions"], pathSTORIES["Exposition"][expositionPosition]["Story"])

            evaulate_action(story_bit, choice_array,
                            pathSTORIES["Exposition"][expositionPosition]["Uniques"]["ID"],
                            "Exposition", choicesObj, player_Obj)
            expositionPosition += 1

        # Monster Encounter
        elif story_chunk[0] == "M":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["Monster"][monsterPosition]["Actions"], pathSTORIES["Monster"][monsterPosition]["Story"])

            evaulate_action(story_bit, choice_array,
                            pathSTORIES["Monster"][monsterPosition]["Uniques"]["ID"],
                            "Monster", choicesObj, player_Obj)
            monsterPosition += 1

        # Mini Boss Encounter
        elif story_chunk[0] == "Mi":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["miniBoss"]["Actions"], pathSTORIES["miniBoss"]["Story"])
            evaulate_action(story_bit, choice_array,
                            pathSTORIES["miniBoss"]["Uniques"]["ID"],
                            "miniBoss", choicesObj, player_Obj)

        # Scenario  - 1
        elif story_chunk[0] == "S1":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["Scenario-1"]["Scenarios"][scenarioOnePosition]["Actions"], pathSTORIES["Scenario-1"]["Scenarios"][scenarioOnePosition]["Story"])

            evaulate_action(story_bit, choice_array,
                            pathSTORIES["Scenario-1"]["Scenarios"][scenarioOnePosition]["Uniques"]["ID"],
                            "Scenario-1", choicesObj, player_Obj)
            scenarioOnePosition += 1

        # Scenario  - 2
        elif story_chunk[0] == "S2":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["Scenario-2"]["Scenarios"][scenarioTwoPosition]["Actions"], pathSTORIES["Scenario-2"]["Scenarios"][scenarioTwoPosition]["Story"])

            evaulate_action(story_bit, choice_array,
                            pathSTORIES["Scenario-2"]["Scenarios"][scenarioTwoPosition]["Uniques"]["ID"],
                            "Scenario-2", choicesObj, player_Obj)
            scenarioTwoPosition += 1

        # Scenario  - 3
        elif story_chunk[0] == "S3":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["Scenario-3"]["Scenarios"][scenarioThreePosition]["Actions"], pathSTORIES["Scenario-3"]["Scenarios"][scenarioThreePosition]["Story"])

            evaulate_action(story_bit, choice_array,
                            pathSTORIES["Scenario-3"]["Scenarios"][scenarioThreePosition]["Uniques"]["ID"],
                            "Scenario-3", choicesObj, player_Obj)
            scenarioThreePosition += 1

        # Boss Encounter
        elif story_chunk[0] == "B":
            story_bit, choice_array, choicesObj = pathActionTemplate(
                story_chunk[1], pathSTORIES["Boss"]["Actions"], pathSTORIES["Boss"]["Story"])
            print(f'action was {action}\n')
            evaulate_action(story_bit, choice_array,
                            pathSTORIES["Boss"]["Uniques"]["ID"],
                            "Boss", choicesObj, player_Obj)

        position += 1
        pathSTORIES["storyPosition"] = position
        pathSTORIES["expositionPosition"] = expositionPosition
        pathSTORIES["monsterPosition"] = monsterPosition
        pathSTORIES["scenarioOnePosition"] = scenarioOnePosition
        pathSTORIES["scenarioTwoPosition"] = scenarioTwoPosition
        pathSTORIES["scenarioThreePosition"] = scenarioThreePosition

    pass


""" Driver Code """
# readPathStory(writePath())
# print(
#     f'pathSTORIES["scenarioThreePosition"] {pathSTORIES["scenarioThreePosition"]}')

# test = {'length': 10, "Scenario": "The Castle",
# "Choices": ["Continue", "2", "3", "Back"]}
# print(test)
# random.shuffle(test["Choices"])
# print(test["Choices"])

""" Driver Code 1"""
# llist = LinkedList()
# llist.prepend(4)
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.prepend(5)
# print(llist.head.value)
# print(llist.head.next.value)
# print(llist.show_list())
