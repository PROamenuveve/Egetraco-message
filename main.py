from kivy import Config
Config.set('graphics', 'width', '280')
Config.set('graphics', 'height', '524')

import os 
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.app import MDApp
import plyer
from plyer import utils
import json
import datetime
# from kivymd.uix.imagelist import SmartTileWithLabel
# from kivymd.uix.chip import MDChooseChip
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.properties import NumericProperty, Clock, BooleanProperty , ObjectProperty, StringProperty
from kivymd.uix.list import IconLeftWidget,TwoLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivy.logger import Logger
from kivy.uix.behaviors.compoundselection import CompoundSelectionBehavior
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty,NumericProperty,BooleanProperty,ObjectProperty
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.bottomsheet import MDListBottomSheet,MDGridBottomSheet
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.snackbar import Snackbar
from kivy.uix.button import Button
from kivymd.uix.list import OneLineListItem,TwoLineListItem
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.fitimage import FitImage
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.animation import Animation
from kivymd.uix.button import MDIconButton
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import  Screen
from akivymd.uix.dialogs import AKAlertDialog
from akivymd.uix.datepicker import AKDatePicker


from recuperation import les_donners
from base_de_donner import La_base_de_donner

KV = '''
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "nom"

    MDTextField:
        hint_text: "prenom"
'''

class PageInscription(MDScreen):
    
    titre = StringProperty()
    test = StringProperty()
    nom = StringProperty()
    prenom = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def suivant(self):
        
        self.nom =  self.ids.nom.text
        self.prenom = self.ids.prenom.text
        if self.nom == "":
            self.ids.nom.error = True
            self.ids.nom.helper_text = "veiller enter votre nom"
            # self.ids.btn.grow()
            self.ids.btn.shake()
        else:
            if self.prenom == "":
                self.ids.prenom.error = True
                self.ids.prenom.helper_text = "veiller enter votre prenom"
                self.ids.btn.shake()
            else:
                self.parent.parent.push("Information")
                self.ids.btn.grow()
                print(self.nom)
                
            #and prenom !=  ""
    # def retour(self):
    #     return ({"nom":self.ids.nom.text,"prenom":self.prenom})

class Information(MDScreen):
    utilisateur = []
    def __init__(self,**kw):
        super().__init__(**kw)
        self.date = AKDatePicker(callback=self.datte)
        self.date.max_year = 2023
 
    def datte(self,date):
        if not date :
            return
        self.ids.date.text = "%d / %d / %d" % (date.day, date.month, date.year)
        
    def open(self):
        self.date.open() 
    def suivant(self):
        self.age=  self.ids.age.text
        self.numero = self.ids.numero.text
        try :int(self.age)
            
        except:
            self.ids.age.error = True
            self.ids.age.helper_text = "entrer l' age en entier"
            self.ids.btn.shake()
        else:
            if self.age== "":
                pass
            else:
                try :int(self.numero)
            
                except:
                    self.ids.numero.error =True
                    self.ids.numero.helper_text = "entre votre numero de telephone valide"
                    self.ids.btn.shake()
                else:
                    if len(self.numero) < 8 :
                        self.ids.numero.error =True
                        self.ids.numero.helper_text = "entre votre numero de telephone valide"
                        self.ids.btn.shake()
                    else:
                        numeros = list(self.numero)
                        if int(numeros[0]) <6:
                            self.ids.numero.error =True
                            self.ids.numero.helper_text = "entre votre numero de telephone valide"
                            self.ids.btn.shake()
                        else:
                            self.parent.parent.push("Messages")
                            self.ids.btn.grow()
                            nom=PageInscription().nom
                            prenom=PageInscription().prenom
                            # print(info)
                            if self.ids.homme.active:
                                sexe = "homme"
                            elif self.ids.femme.active:
                                sexe = "femme"
                            else:
                                sexe = "non definie"

                            self.utilisateur = ({"nom":nom,"prenom":prenom,
                                        "age":self.age,"numero_de_telephone":self.numero,
                                        "sexe":sexe})
                            La_base_de_donner().creer_utilisateur(self.utilisateur)
    def retour(self):
        return {"age":self.age,"numero":self.numero}
class Utilisateur():
    nom = ""
    prenom = ""
    age = "nom definis"
    numero_de_telephone = ""
    sexe = "non definie"
    les_utiisateurs  = []
    def __init__(self) :
        info = Information().utilisateur
        print(info)
        # self.nom = info["nom"]
        # self.prenom = info["prenom"]
        # self.age = info["age"]
        # self.sexe = info["sexe"]

class Connection(MDScreen):
    pass

class MotsDePasseOublier(MDScreen):
    pass

class MotsDePasse(MDScreen):
    def suivant(self):
        motsA = self.ids.motsA.text
        motsB = self.ids.motsB.text
        if len(motsA ) <=7:
            self.ids.motsA.error =True
            self.ids.motsA.helper_text = "entre un mots de passe avec plus 8 caracters"
            self.ids.btn.shake()
        else:
            if motsA ==  motsB:
                self.parent.parent.push("Messages")
                self.ids.btn.grow()
            else:
                self.ids.motsB.error =True
                self.ids.motsB.helper_text = " mots de passe nom identique"
                self.ids.btn.shake()



class MenuPrincipal(MDScreenManager):
    Personne_utiisateur = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screens_name = "Messages"
        # self.transition.duration = .2
        # try:
        #     with open ("Personne_utiisateu.json","r") as f:
        #         self.Personne_utiisateur  = json.load(f)
        # except: 
        #     self.current = "PageInscription"
        # else:
        # #    self.current = "Messages" 
        # pass
    screen_stack = []
    # pas = 1
    # pase = 0
    def passe(self):
        self.push(self,"Message")
    def push(self, screen_name):
        # self.screens.name = "Message"
        # self.pas += 1
        # if self.pas >= 2:
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.transition.duration = .1
            # self.transition.transitiom =" Wipe"
            self.current = screen_name

    def pop(self):
        if Message.ok:
            if len(self.screen_stack) > 0:
                screen_name = self.screen_stack[-1]
                del self.screen_stack[-1]
                self.transition.direction = "right"
                self.transition.duration = .1
                self.current = screen_name
    # def printe(self,pa):
        
    #     print("--------------------------------")
    #     self.push(pa)
    #     print("********************************")
    
      
class MessageItem(MDCard):
    nom = StringProperty()
    prenom = StringProperty()
    message = StringProperty()
    nmessage = StringProperty()
    date = StringProperty()
    image = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def renvoie(self,txt):
        # Personne().messagee(txt)
        # print(txt)
        pass

class Entete  (MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tool = "init"
        self.radius = ("0dp","0dp","10dp","10dp")
    
    def parente(self): 
        self.tools(self.tool) 
    def  go(self):
        print("go")
    def tools(self,typ):
        # self.clear_widgets()
        self.typ = typ
        if self.typ == "init":
            self.remove_widget(self.ids.tool_recherche)
            # self.add_widget(self.ids.tool_bar)
            # pass
        elif self.typ == "tool_bar":
            self.remove_widget(self.ids.tool_recherche)
            self.add_widget(self.ids.tool_bar)
        elif self.typ == "recherche":
            self.remove_widget(self.ids.tool_bar)
            self.add_widget(self.ids.tool_recherche)
            
    # def tools(self,type):
    #     # self.type = "init"
    #     self.ids.clear_widgets()
    #     if self.type == "init":
    #         self.ids.add_widget(self.ids.tool_bar)
    #     elif self.type == "tool_bar":
    #         # self.remove_widget(self.ids.tool_recherche)
    #         self.add_widget(self.ids.tool_bar)
    #     elif self.type == "recherche":
    # #         self.remove_widget(self.ids.tool_bar)
    #         self.add_widget(self.ids.tool_recherche)
    
           
class Messages(MDBoxLayout):
    laListe = []
    donner = []
    items = []
    mode = ""
    photo = ""
    nom = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = MDDialog()
        # Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.mode = "messages"
        d = les_donners().get_donner()
        for i in d:
            self.nom= i["nom"]
            prenom=i["prenom"]
            age=i["age"]
            self.photo=i["photo"]
            sexe=i["sexe"]
            profession=i["profession"]
            description=i["description"]
            message_de_description=i["message_de_description"]
            profile=i["profile"]
            message=i["message"]
            dernier_message = message[-1]["message"]
            dernier_date = str(message[-1]["date"])
            self.laListe.append ({"nom":self.nom,"prenom":prenom,"age":age,"photo":self.photo,"sexe":sexe,
                "profession":profession,"description":description, "message_de_description":message_de_description,
                "profile":profile, "message":message, "dernier_message":dernier_message,"date":str(dernier_date.split(" "))})
        for d in self.laListe:
            print(dernier_date)
            self.donner.append({"image":d["photo"],"nom":d["nom"],"message":d["dernier_message"],
                                "date":str(0),"nmessage":str(len(d["message"]))})
            # print(d["nom"],"\n")
        # self.update()
            # m = list(d["dernier_message"])
            # print(len(m))
        # print(d["dernier_message"].size())
    def parente ( self):
        self.update()
        pass
    def update(self):
        self.ids.View.data = self.donner

        # for d in self.laListe:
        #     print("d")

            # self.ids.list_de_messages.add_widget(Click
            #     (FitImage(size_hint_x= None,size_hint_y= None,height= dp(54),width= dp(54),radius=dp(27),
            #               source = d["photo"]),
            #     (TwoLineListItem(
            #         text= d["nom"],secondary_text= d["dernier_message"] ,id= "tow")),
            #     (MDBoxLayout(
            #         Label(text= "date",color = "blue"),
            #         MDCard(Label(text=str( len(d["message"]))),size_hint_x= None,size_hint_y= None,height= dp(28),
            #                width= dp(28),radius=[dp(14),dp(14)],md_bg_color="blue",),
            #         orientation=  'vertical',size_hint_x= .2)),
            #     size_hint_y=  None, height= dp(56)),)
    
    def modes(self,x):
        pass
        if x == "recherche":
            # self.ids.list_de_messages.clear_widgets()
            # self.ids.list_de_messages.add_widget(MDLabel(text="ldsaaa"))
            # # print("clear")
            self.ids.View.data = []
        elif x == "tool_bar":
            self.ids.View.data = self.donner
            
    def set_recherche(self,text):
        # print(text)
        self.items = []
        self.iteme = []
        # self.unique_sweets = []
        def lenom(items):
            return items["nom"]
        if len(text) == 1:
            for item in self.donner:
                if text.lower()   in item["nom"] or text.capitalize()  in item["nom"]  :#or text in item["nom"]:.isupper()
                    self.iteme.append(item)
        elif len(text) >1:
            for item in self.donner:
                if  text.upper()  in item["nom"] or text.lower()  in item["nom"]:#or text in item["nom"]:.isupper()
                    self.iteme.append(item)
        for sweet in self.iteme:
            if sweet not in self.items:
                self.items.append(sweet)
        self.ids.View.data =self.items
    def Voir(self):


        bottom = MDListBottomSheet()
        bottom.radius_from = ("top" )
        for i in range(15):
            bottom.add_item(
               f"Standart Item {i}",
            lambda x, y=i:None,icon="message"
            )


        bottom.open()
    def select_with_key_down():
        print("select")
        
    def afficer_image(self,m,i):
        self.dialog = MDDialog(
            title =m,
            padding= 0,
            pos_hint={"center_x" :.5},
            # spacing = (0,0,0),
            type = "custom",
            content_cls= MDBoxLayout(
                FitImage(source =i),
                 MDScreen(MDIconButton(
                    icon= "content-save",
                    pos_hint={"center_x" :.5,"center_y" :.3},
                    theme_icon_color= "Custom",
                    icon_color="blue"
                ),size_hint_y= None,
                height= "40dp"),
                orientation= 'vertical',
                size_hint= (None,None),
                height= "220dp",width= "180dp"),
        )
        self.dialog.open()
         
    def Dialog(self):
        # self.dialog = MDDialog()
        
        bton = [MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                text_color="green",
                on_release= lambda x="parametre":self.dialog.dismiss()

             ),
            MDFlatButton(
                text="ACCEPT",
                theme_text_color="Custom",
                text_color="green",
                # on_press = self.dialog.dismiss()
                
            ),]
        self.dialog =  MDDialog(
            title = "recherche",
            text = "voulez vraiment faire une recherche ???",
            buttons= (bton)
                            ,
        )

        self.dialog.open()
  
    # def diss(self):
    #     self.Dialog("P")
    # def toals(self,type):
        # self.ids.tool.tools(type)  
        
    def callback(self, button):  

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "arcive",
                "height": dp(56),
                "on_release": lambda x=None:None,
             } ,
            {
                "viewclass": "OneLineListItem",
                "text": "marquer comme lue",
                "height": dp(56),
                "on_release": lambda x=None: None,
             } ,
            {
                "viewclass": "OneLineListItem",
                "text": "parametre",
                "height": dp(56),
                "on_release":lambda x="parametre":(self.parent.parent.push("Parametre"),self.menu.dismiss())
             } ,
                    ]
        self.menu = MDDropdownMenu( 
                   items=menu_items,
                width_mult=2,
                                       )
        self.menu.caller = button
        self.menu.open()

class Message(MDBoxLayout):
    selection_list = []
    li = []
    appui = True
    ok = True
    overlay_color = get_color_from_hex("#66EE88")
    def parente ( self):
        d = les_donners().get_donner()
        for i in d:
            nom= i["nom"]
            prenom=i["prenom"]
            age=i["age"]
            photo=i["photo"]
            sexe=i["sexe"]
            profession=i["profession"]
            description=i["description"]
            message_de_description=i["message_de_description"]
            profile=i["profile"]
            message=i["message"]
            dernier_message = message[-1]["message"]
        # self.ids.selection_list.unselected_all()
        # for i in range(25):
            self.ids.selection_list.add_widget(Click
                (FitImage(size_hint_x= None,size_hint_y= None,height= dp(54),width= dp(54),radius=dp(27),
                          source = photo),
                (TwoLineListItem(
                    text= nom,secondary_text= dernier_message)),
                (MDBoxLayout(
                    Label(text= "date",color = "blue"),
                    MDCard(Label(text=str( len(message))),size_hint_x= None,size_hint_y= None,height= dp(28),
                           width= dp(28),radius=[dp(14),dp(14)],md_bg_color="blue",),
                    orientation=  'vertical',size_hint_x= .2)),
                size_hint_y=  None, height= dp(56),),)
            
            # self.ids.selection_list.add_widget(MDBoxLayout(MDBoxLayout(Label(text=(f"salut n {i}"  )))))
            # self.li.append({"nom":"nom"})
            # print("nnnnnnnnnnnnnnnnnnnnn")
      
        # self.selection_list.data = self.li
    def unselected(self):
        self.ids.selection_list.unselected_all()
          
        
    def fonct(self):
        print("fonct")
        
    def set_selection_mode(self, instance_selection_list, mode):
        ic = MDIconButton(icon= "close",
                pos_hint= {"center_x": .1, "center_y": .5})
        if mode:
            self.appui = False
            self.ok = False
            MenuPrincipal.pas = 0
            # print(self.ok)
            # ic =
            self.ids.anuler.icon = "close"
            self.ids.labele.text = "0"
            self.ids.labele.pos_hint = {"center_x": .4, "center_y": .5}
            self.ids.magnify.icon = "trash-can"
            self.ids.vertical.icon = "dots-vertical"
            md_bg_color = self.overlay_color,
            # self.selcte = True ,
        #     left_action_items = [
        #         [
        # "close",
        # lambda x: self.ids.selection_list.unselected_all(),
        #                 ]
        #             ]
        #     right_action_items = [["trash-can"], ["dots-vertical"]]
           
        else:
            self.appui = True
            self.ok = True
            # MenuPrincipal.pas = 
            # self.ids.tool.remove_widget(ic)
            self.ids.labele.text = "EGETRACO"
            self.ids.labele.pos_hint = {"center_x": .3, "center_y": .5}
            self.ids.magnify.icon ="magnify"
            self.ids.vertical.icon = "dots-vertical"
            md_bg_color =(.2,.7,.25,1)
            # left_action_items = []
            # right_action_items = [["magnify", lambda x: self.parent.parent.push("Recherche"), #self.parent.parent.push("Recherche"),
            #                        "recherche"], ["dots-vertical", lambda x: self.callback(x),"plus"]]
            
        # self.ids.bar.title = "EGETRACO"
        Animation(md_bg_color=md_bg_color, d=0.3).start(self.ids.tool)
        # self.ids.bar.left_action_items = left_action_items
        # self.ids.bar.right_action_items = right_action_items

    def on_selected(self, instance_selection_list, instance_selection_item):
        self.ok = False
        self.ids.tool.text = str(
        len(instance_selection_list.get_selected_list_items())
                )
    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.ids.tool.text  = str(
            len(instance_selection_list.get_selected_list_items())
                )
    def xx (self):
        if self.appui:
            print("gjzzfzzzzzzzzzzzzzzz")

    def Voir(self):

        bottom = MDListBottomSheet()
        bottom.radius_from = ("top" )
        for i in range(15):
            bottom.add_item(
               f"Standart Item {i}",
            lambda x, y=i:None,icon="message"
            )
        # bottom.duration_opening = 1
        # bottom.animation =True
        bottom.open()

    def Dialog(self):

        self.dialog = MDDialog()
        
        self.dialog(
            title = "recherche",
            text = "voulez vraiment faire une recherche ???",
            buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                text_color="green",

             ),
            MDFlatButton(
                text="ACCEPT",
                theme_text_color="Custom",
                text_color="green",
            ),
        ],
        )
        self.dialog.open()
        
    def callback(self, button):  

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "arcive",
                "height": dp(56),
                "on_release": lambda x=None:None,
             } ,
            {
                "viewclass": "OneLineListItem",
                "text": "marquer comme lue",
                "height": dp(56),
                "on_release": lambda x=None: None,
             } ,
            # {
            #     "viewclass": "OneLineListItem",
            #     "text": "profile",
            #     "height": dp(56),
            #     "on_release": lambda x="profile":(self.parent.parent.push("Profile"),self.menu.dismiss()),
            #  } ,
            {
                "viewclass": "OneLineListItem",
                "text": "parametre",
                "height": dp(56),
                "on_release":lambda x="parametre":(self.parent.parent.push("Parametre"),self.menu.dismiss())
             } ,
                    ]
        self.menu = MDDropdownMenu(
                   items=menu_items,
                width_mult=3,
                                       )
        self.menu.caller = button
        self.menu.open()

    def parametre(self):
        print("ok")
    #    self.ids.mesg.parent.parent.push("Parametre")



class Profile(MDBoxLayout):
    photo = StringProperty()
    nom = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.photo = ""
        self.nom = ""
        
    def tof(self,p,n):
        self.photo = p
        self.nom = n
class LesMessage(MDBoxLayout):
    personne = StringProperty()
    message = StringProperty()
    # date = NumericProperty()
    suiprimer= BooleanProperty()

class Personne(MDBoxLayout):
    clef = StringProperty()
    photo = StringProperty()
    message = StringProperty()
    info = StringProperty()
    date = StringProperty()
    suiprimer= BooleanProperty()
    laListe = []
    nom = StringProperty("")
    inf = StringProperty()
    li = []
    lis = []
    # noms = ["amenuveve","josianne","NOSSI","jacque","rose","MOUSSA","jean"]
    z = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clef = ""
        self.nom = ""
        self.photo = ""  
    def cl(self):
        self.ids.Les_Message.clear_widgets()
    def parente(self):
        # self.messagee(self.noms[self.z])
        # self.z += 1
        # self.ids.Les_Message.add_widget(MDBoxLayout(MDLabel(text="salut")))
        # self.messagee(self.nom)
        print("parent")
        
        pass
    # def ItemMessage(self,info):
    #     self.uppdate(info)
    #     print(info)
        # self.inf = info
    def uppdate(self,info):
        print(info,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # self.ids.Les_Message.add_widget(MDBoxLayout(MDLabel(text="salut")))
     
    def okk(self):
        print("okk")
        
    def messagee(self,info):
        self.nom = info
        self.info = info
        self.ids.Les_Message.clear_widgets()
        # print("chargement...........")
        (self.lis,photo) = les_donners().personne(info)
        self.photo = photo
        if self.lis :
            # print(len(self.lis))
            for i in self.lis :
                self.personne = i["personne"]
                self.message = i["message"]
                self.datee = i["date"]
                # print(self.datee)
                self.suiprimer = i["suprimer"]
                # self.li.append({"personne":self.personne,"message":self.message,
                #                 "date":self.date,"suiprimer":self.suiprimer})
                m = list(i["message"])
                msg = i["message"].split("\n")
                # print(msg)
                gmots = 0
                for mots in msg:
                  pmots = len(mots)  
                  if pmots > gmots:
                      gmots = pmots
                    
                # print(m)
                # larguer = len(m)*10
                larguer = gmots*10
                if larguer > 180:
                    larguer = 180
        
                if self.personne == "mois":
                    # print("mois+++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    self.ids.Les_Message.add_widget(MDBoxLayout(MDLabel(),MDBoxLayout(MDLabel(text = self.message,
                            size_hint=( None, None),adaptive_height=True,width=dp(larguer))

                            ,md_bg_color=EgetracoApp().theme_cls.primary_dark,size_hint=( None, None),adaptive_height=True,width=(dp(larguer)+dp(10)),radius= dp(10),
                            padding=('8dp', '8dp', '8dp', '8dp') ),
                                size_hint=( 1, None),adaptive_height=True))

                elif self.personne == "lui":
                    self.ids.Les_Message.add_widget(MDBoxLayout(MDBoxLayout(MDLabel(text = self.message,
                            size_hint=( None, None),adaptive_height=True,width=dp(larguer))

                            ,md_bg_color=EgetracoApp().theme_cls.primary_dark,size_hint=( None, None),adaptive_height=True,width=(dp(larguer)+dp(10)),radius= dp(10),
                            padding=('8dp', '8dp', '8dp', '8dp') ),MDLabel(),
                                size_hint=( 1, None),adaptive_height=True ))

                else:
                    self.ids.Les_Message.add_widget(MDBoxLayout(MDLabel(),MDBoxLayout(MDLabel(text = self.message,
                            size_hint=( None, None),adaptive_width=True,height=dp(25))

                            ,md_bg_color=EgetracoApp().theme_cls.primary_dark,size_hint=( None, None),adaptive_width=True,height=dp(35),radius= dp(5),
                            padding=('4dp', '4dp', '4dp', '4dp') ),MDLabel(),
                            size_hint=(1, None),adaptive_height=True))#,width=("28dp")
            # self.ids.Recycl.data =self.li
            self.ids.Les_Message.add_widget(MDBoxLayout(size_hint_y =None,
                                            height= "70dp"))
                        
    # break
    
    def envoie(self,Lmessage):
        if Lmessage:
            print(Lmessage)
            self.lis.append({"personne": "mois","message": Lmessage,
              "date": str(datetime.datetime.now()),"suprimer": False})
            les_donners().modification(self.info,self.lis)
            self.ids.message_entrer.text = ""
            self.messagee(self.info)

class Click(MDCard,Button):
    def renvoie(self,txt):
        Personne().appeler(txt)
        print(txt)

class Recherche(MDBoxLayout):
    pass
            
class SuperDialog(Popup,MDBoxLayout):
    pass
class Parametre(MDBoxLayout,Utilisateur):
    nom = StringProperty()
    prenom = StringProperty()
    numero_de_telephone= StringProperty()
    adress_email = StringProperty()
    adress_local = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nom ="NOSSI"
        self.prenom ="komlan"
        self.numero_de_telephone = "96 76 08 26"
        self.adress_local = "non definie"
        self.adress_email="non definie"
    def Pope(self):
        # self.Pop =SuperDialog(Label= "NOSSI")
        # self.Pop.title = "popup "
        pass
        # self.Pop.open()
        
    def le_parent(self):
        pass
    def opac(self):
        print("clik")
    def num(self):
        # self.Dialog().dialog.dismiss()
        # self.Dialog()
        self.dialoge = MDDialog(
            title = "Modification",
            text = "un SMS vous serra envoiez sur votre numero pour la confirmation de la modification",
            buttons=[
                MDFlatButton(
                    text= "ok",
                    on_release= lambda x="parametre":self.dialog.dismiss(),
                    theme_text_color="Custom",
                    text_color="green",
                ),]
        )
        self.dialoge.open()
    def Dialog (self):
        self.dialog = MDDialog(
            title ="Modification",
            type = "custom",
            content_cls= MDBoxLayout(
                MDTextField(hint_text="nom"),
                MDTextField(hint_text="prenom"),
                
                # MDLabel(text="salut"),
                # MDLabel(text="salut"),
                orientation="vertical"
                ,size_hint_y= None,
                height= "100dp"),
            buttons=[
                MDFlatButton(
                    text= "ANULER",
                    on_release= lambda x="parametre":self.dialog.dismiss(),
                    theme_text_color="Custom",
                    text_color="green",
                ),
                MDFlatButton(
                    text= "MODIFIER",
                    on_release= lambda x="parametre":self.num(),
                    on_press =lambda x="parametre":self.dialog.dismiss(), # [ lambda x = "x": self.num(), ],#[lambda x="":self.dialog.dismiss()],],
                    theme_text_color="Custom",
                    text_color="green",
                   
                ),
            ]
        )
        # if self.dialog.on_dismiss():
        #     self.dialog.dismiss()
        # else:
        self.dialog.open()
        
class Modifications(MDBoxLayout):
    nom = StringProperty()
    prenom = StringProperty()
    numero_de_telephone= StringProperty()
    adress_email = StringProperty()
    adress_local = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nom ="NOSSI"
        self.prenom ="komlan"
        self.numero_de_telephone = "96 76 08 26"
        self.adress_local = "non defini"
    def valide(self):
        pass

class EgetracoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.name = "E-Message"
        self.theme_cls.theme_style ="Light"#"Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
    def theme(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"


# if __name__ =='__name__':
EgetracoApp().run()
