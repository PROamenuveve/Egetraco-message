import json 

class les_donners:
    nom = ""
    personne = ""
    date = 0
    suprimer = False
    mon_profile = []
    les_amies = []
    donner = []
    perso_liste = []
    def __init__(self):
        with open ("fichier.json","r") as f:
            self.donner = json.load(f)
        self.les_amies = self.donner["Profile"]["Amies"]
        # print(self.les_amies)
    def get_donner(self):
        return self.les_amies
        # print(self.les_amies)
        # print(self.les_amies[8])
    def personne(self,perso):
        self.perso_liste = []
        for i in self.les_amies:
            if i["nom"] == perso:
                # print(perso,"!!!!!!!!")
                # print(i)
                photo= i["photo"]
                for p in i["message"] :
                    # print(p)
                    self.perso_liste.append({"personne":p["personne"],"message":p["message"],
                    "date":p["date"],"suprimer":p["suprimer"]})
                    # print(self.perso_liste,"-------------")
                return (self.perso_liste,photo)
    def modification(self,le_nom,le_contenue):
        for i in self.les_amies:
            if i["nom"] == le_nom:
                # print("modification")
                i["message"] = le_contenue
                # ma_liste_en_json = json.dumps(ma_liste)
                with open("fichier.json","w") as f:
                    json.dump(self.donner,f, indent=2 )
                break    
                    
                    
        

# les_donners()
