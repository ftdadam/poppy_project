import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

#Configuration de l'input TUIO
Config.set('input','Reactable','tuio,127.0.0.1:3333')

class Table(FloatLayout):

	mainButton = Button(text="Test1", font_size=14)
	

	#mainButton.bind(on_press=self.callback)

	def __init__(self, **kwargs):
		super(Table, self).__init__(**kwargs)
		self.size_hint = (1,1)    
		self.add_widget(self.mainButton)
		self.mainButton.size_hint=(0.05,0.02)
		self.mainButton.pos_hint={'center_x': 0.5,'center_y': 0.5}
		self.mainButton.bind(on_press=self.callback)
        
        #self.mainLampButton.bind(on_release=self.removeButtons)

	def callback(instance,button):
		#print(instance,button)
		print('The button <%s> is being pressed' %button.text)


class MyApp(App):

    def build(self):
        return Table()


if __name__ == '__main__':
    MyApp().run()