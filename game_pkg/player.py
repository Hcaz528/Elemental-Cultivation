class Player:
    # Class attributes
    # amount = 0

    def __init__(self, Name=None, Inventory={}, Power=100, Max_Power=100, HP=100, Elemental_Set={'1': "Fire", '2': "Lightning",
                                                                                                 '3': "Wind"}):
        self.Name = Name if not None else "Chadwick"
        self.Inventory = Inventory
        self.Current_Power = Power
        self.Max_Power = Max_Power
        self.Current_HP = HP
        self.Elemental_Set = Elemental_Set
        self.Cultivation = 0
        self.Max_HP = 100

    def modify_Name(self, value):
        self.Name = value

    def modify_Inventory(self, value):
        self.Inventory = value

    def modify_Power(self, value):
        self.Current_Power = value

    def modify_Max_Power(self, value):
        self.Max_Power = value

    def modify_HP(self, value):
        self.Current_HP = value

    def modify_Elemental_Set(self, value):
        self.Elemental_Set = value

    def returnPersonDict(self):
        return {
            "Name": self.Name,
            "Inventory": self.Inventory,
            "Power": self.Current_Power,
            "Max_Power": self.Max_Power,
            "HP": self.Current_HP,
            "Max_HP": self.Max_HP,
            "Elemental_Set": self.Elemental_Set,
            "Cultivation": self.Cultivation,
        }

    def fullLoadPersonDict(self, Dict):
        self.Name = Dict["Name"]
        self.Inventory = Dict["Inventory"]
        self.Current_Power = Dict["Power"]
        self.Max_Power = Dict["Max_Power"]
        self.Current_HP = Dict["HP"]
        self.Elemental_Set = Dict["Elemental_Set"]
        self.Cultivation = Dict["Cultivation"]
        self.Max_HP = Dict["Max_HP"]
