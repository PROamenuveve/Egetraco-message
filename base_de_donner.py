import json 

class La_base_de_donner:
    nom = ""
    prenom = ""
    age = "nom definis"
    numero_de_telephone = ""
    sexe = "non definie"
    les_utiisateurs  = []
    def __init__(self) :
        try:
            with open ("utilisateurs.json","r") as f:
                self.les_utiisateurs  = json.load(f)
        except: 
            None
    def creer_utilisateur(self,utilisateur):
        self.les_utiisateurs.append({"nom":utilisateur["nom"],"prenom":utilisateur["prenom"],
            "age":utilisateur["age"],"numero_de_telephone":utilisateur["numero_de_telephone"],
            "sexe":utilisateur["sexe"]})
        with open("utilisateurs.json","w") as f:
            json.dump(self.les_utiisateurs,f, indent=2 )
            print("ajouter")
    def se_connecter(self,nom,num):
        for i in self.les_utiisateurs:
            if nom == i["nom"] and  num == i["numero_de_telephone"]:
                return i
        return "le nom n'est pas trover !"
        
        
    
    