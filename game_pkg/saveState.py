import json
import time


def current_milli_time():
    return round(time.time() * 1000)


def loadGameSave(location='saveFile.json'):
    JSONContents = ''
    with open(location) as f:
        # It reads it and then loads the json
        JSONContents = json.loads(f.read())
    return JSONContents


def createOrUpdateGameFile(contents=None, mainPathDict=None, subPathDict=None, location='saveFile.json'):
    """
    Structure
        {
            'Name': "The Name",
            'HP': 100,
            'AP': 100,
            'Max_Power': 100,
            'save_date': 0,
            'base_def': 50,
            'base_dodge': 25,
            'SkillSet': {'1': "Power_1", '2': "Power_2", '3': "Power_3"},
            'Inventory': {"Item_1": 0, "Item_2": 0, "Item_3": 0},
            "Path_Position": "",
            "Sub_Path_Position": "",
            "Sub_Path": {'length': 10, "Scenario": "The Castle", "Scenarios": [{"Enemy": "Dead", "Choices": ["Continue", "2", "3", "Back"]}, {"Enemy": "Goblin", "Choices": ["Fight", "Flee"]}]},
            "Main_Path": {'length': 10, 'Scenarios': ["Peat", "Petunia", "Yo Dawg"]}
        }
    """
    contents_json = ""
    if not(contents == None):
        content["Sub_Path"] = subPathDict
        content["Main_Path"] = mainPathDict
        print(contents)
    else:
        contents = {
            'Name': "The Name",
            'HP': 100,
            'AP': 100,
            'Max_Power': 100,
            'save_date': 0,
            'base_def': 50,
            'base_dodge': 25,
            'SkillSet': {'1': "Power_1", '2': "Power_2", '3': "Power_3"},
            'Inventory': {"Item_1": 0, "Item_2": 0, "Item_3": 0},
            "Path_Position": "",
            "Sub_Path_Position": "",
            "Sub_Path": {'length': 10, "Scenario": "The Castle", "Scenarios": [{"Enemy": "Dead", "Choices": ["Continue", "2", "3", "Back"]}, {"Enemy": "Goblin", "Choices": ["Fight", "Flee"]}]},
            "Main_Path": {'length': 10, 'Scenarios': ["Peat", "Petunia", "Yo Dawg"]},
            "Sub_Scenarios_Left": {'length': 10, "Scenario": "The Castle", "Scenarios": [{"Enemy": "Dead", "Choices": ["Continue", "2", "3", "Back"]}, {"Enemy": "Goblin", "Choices": ["Fight", "Flee"]}]},
            "Main_Secnarios_Left": {'length': 10, 'Scenarios': ["Peat", "Petunia", "Yo Dawg"]}
        }

    contents["save_date"] = current_milli_time()
    contents_json = json.dumps(contents, indent=4)
    f = open(location, "w")
    f.write(contents_json)
    f.close()


def updateGameFile(contents, location='saveFile.json'):
    # Changing dictionary to JSON
    contents = json.dumps(contents, indent=4)

    f = open(location, "w")
    f.write(contents)
    f.close()


subPath = {'length': 5, "Scenario": "The Stronghold", "Scenarios": [{"Enemy": "Dead", "Choices": [
    "Continue", "2", "3", "Back"]}, {"Enemy": "Not Goblin", "Choices": ["Fight", "Flee"]}]}
mainPath = {'length': 12,
            'Scenarios': ["Yolanda", "The Ever Lasting", "Yo Dawg"]}

createOrUpdateGameFile()
content = loadGameSave()
print(content['Name'])
content['Name'] = "Joe Stoe"
del content["Sub_Path"]
del content["Main_Path"]

createOrUpdateGameFile(content, mainPath, subPath)

content = loadGameSave()
print(content['Name'])
