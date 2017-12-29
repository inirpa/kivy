from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line

class Widgets(Widget):
	pass

class DrawInput(Widget):
	def on_touch_down(self, touch)	:
		print(touch)
		with self.canvas:
			touch.ud["line"] = Line(points=(touch.x, touch.y))

	def on_touch_move(self, touch)	:
		print(touch)
		touch.ud["line"].points += (touch.x, touch.y)	

	def on_touch_up(self, touch)	:
		print("released",touch)		
	
class SimpleKivy(App):
	def build(self):
		# return Widgets()
		return DrawInput()

if __name__ == "__main__":
	SimpleKivy().run()
