from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class DemoProject(ScreenManager):
	def print_msg(self,root):
		exmaple = self.ids.scrn2 #ncome nota non serve self. cui
		#self.exmaple = self.ids.scrn2
		#print(self.exmaple.text)
		print(exmaple.text)
		root.current = "screen_2"


class Main(MDApp):
	def build(self):
		Builder.load_file("guiProject_wit_fuction.kv")
		return DemoProject()
Main().run()
