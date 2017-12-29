from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line

class Widgets(Widget):
	pass

class TouchInput(Widget):
	def on_touch_down(self, touch)	:
		print(touch)

	def on_touch_move(self, touch)	:
		print(touch)	

	def on_touch_up(self, touch)	:
		print("released",touch)		
	
class SimpleKivy(App):
	def build(self):
		# return Widgets()
		return TouchInput()

if __name__ == "__main__":
	SimpleKivy().run()
