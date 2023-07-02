from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivy.lang import Builder

class Demo1 (Screen):
    pass

class Demo2(Screen) :
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")
        sm = ScreenManager()
        #sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Demo1(name = "demo1"))
        sm.add_widget(Demo2(name = "demo2"))
        return sm

Main().run()