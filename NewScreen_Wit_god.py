from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
class Content(BoxLayout):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Demo(ScreenManager):
    pass

class Main(MDApp) :
    def build(self):
        Builder.load_file("NewScreen_Wit_god.kv")
        return Demo()

Main().run()

