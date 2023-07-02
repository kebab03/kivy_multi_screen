from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class Demo(ScreenManager):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("gui.kv")
        return Demo()

Main().run()