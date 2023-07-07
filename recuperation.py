import json 

class les_donners:
    nom = ""
    personne = ""
    date = 0
    suprimer = False
    mon_profile = []
    les_amies = []
    donner = []
    def __init__(self):
        with open ("fichier.json","r") as f:
            self.donner = json.load(f)
        self.les_amies = self.donner["Profile"]["Amies"]
        # print(self.les_amies)
    def get_donner(self):
        return self.les_amies
        # print(self.les_amies)
        # print(self.les_amies[8])

les_donners()
