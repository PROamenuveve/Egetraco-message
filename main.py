from kivy import Config
Config.set('graphics', 'width', '280')
Config.set('graphics', 'height', '520')

from kivymd.app import MDApp
import plyer
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivymd.uix.list import IconLeftWidget,TwoLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivy.logger import Logger
from kivy.core.window import Window
# from kivy.uix.recycleView import RecycleView
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

from recuperation import les_donners

class Click(MDCard,Button):
    pass
    # def fonct(self):
    #     print("fonction")

class MenuPrincipal(MDScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screens_name = "Message"
        # self.transition.duration = .2
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
            self.transition.duration = .3
            self.current = screen_name

    def pop(self):
        if Message.ok:
            if len(self.screen_stack) > 0:
                screen_name = self.screen_stack[-1]
                del self.screen_stack[-1]
                self.transition.direction = "right"
                self.transition.duration = .3
                self.current = screen_name
    def printe(self,pa):
        
        print("--------------------------------")
        self.push(pa)
        print("********************************")
      
      
        
class Entete  (MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tool = "init"
    
    def parente(self): 
        self.tools(self.tool) 
           
    def tools(self,type):
        self.type = type
        # print("aperler")
        if self.type == "init":
            print("venue")
            self.remove_widget(self.ids.tool_recherche)
            # self.add_widget(self.ids.tool)
        elif self.type == "tool_bar":
            self.remove_widget(self.ids.tool_recherche)
            self.add_widget(self.ids.tool_bar)
        elif self.type == "recherche":
            self.remove_widget(self.ids.tool_bar)
            self.add_widget(self.ids.tool_recherche)
    
          
          
           
class Messages(MDBoxLayout):
            
    def parente ( self):
        # self.tools(self.tool)
        # self.remove_widget(self.ids.tool)
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
            
            
            self.ids.list_de_messages.add_widget(Click
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
           
        self.dialog = MDDialog(
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
        
    def toals(self,type):
        self.ids.tool.tools(type)  
        
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
           
        self.dialog = MDDialog(
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
    pass  
        
class LesMessage(MDBoxLayout):
    nom = StringProperty(None)
  
class Personne(MDBoxLayout):

    def parente(self):
        pass
        for i in range(10):
            self.ids.Les_Message.add_widget(MDBoxLayout(MDLabel(),MDBoxLayout(MDLabel(text = "mes salutation "*8,
                    size_hint=( None, None),adaptive_height=True,width=dp(180))
                                        
                    ,md_bg_color=EgetracoApp().theme_cls.primary_dark,size_hint=( None, None),adaptive_height=True,width=dp(200),radius= dp(20),
                    padding=('8dp', '8dp', '8dp', '8dp') ),
                        size_hint=( 1, None),adaptive_height=True))
                
            self.ids.Les_Message.add_widget(MDBoxLayout(MDBoxLayout(MDLabel(text = "voici ma salutation "*7,
                    size_hint=( None, None),adaptive_height=True,width=dp(180))
                                        
                    ,md_bg_color=EgetracoApp().theme_cls.primary_dark,size_hint=( None, None),adaptive_height=True,width=dp(200),radius= dp(20),
                    padding=('8dp', '8dp', '8dp', '8dp') ),MDLabel(),
                        size_hint=( 1, None),adaptive_height=True ))
                
               
            
            self.ids.Les_Message.add_widget(MDBoxLayout(MDLabel(),MDBoxLayout(MDLabel(text = "la personne ",
                    size_hint=( None, None),adaptive_height=True,width=dp(180))
                                        
                    ,md_bg_color=EgetracoApp().theme_cls.primary_dark,size_hint=( None, None),adaptive_height=True,width=dp(200),radius= dp(5),
                    padding=('8dp', '8dp', '8dp', '8dp') ),MDLabel(),
                        size_hint=( 1, None),adaptive_height=True))
            
            
class Recherche(MDBoxLayout):
    pass
            
class Parametre(MDBoxLayout):
    pass

            
class EgetracoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        
EgetracoApp().run()
