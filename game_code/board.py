import kivy
#kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

#Configuration de l'input TUIO
Config.set('input','Reactable','tuio,127.0.0.1:3333')

class Table(GridLayout):
	def __init__(self, **kwargs):
		super(Table, self).__init__(**kwargs)
		self.turn=0
		self.cols=3
		self.size_hint=(0.7,0.7)
		self.pos_hint={"center_x":0.5,"center_y":0.5}
		
		#This returns the row and column of the button presssed if not already pressed
		def callback(button):
			#print(instance,button)
			i = self.buttons[button]["id"]
			row=i//self.cols
			col=i%self.cols
			#we change colors and return row,col if the button isn't already pressed
			if not(self.buttons[button]["state"]):
				if not(self.turn%2):
					button.background_color=(128,0,0,1)
				else:
					button.background_color=(0,0,128,1)
				self.turn+=1
				self.buttons[button]["state"]=True
				print('Turn: %s' %self.turn)
				print('The button %s (%s,%s) is being pressed' %(self.buttons[button]["id"],row,col))
				return row,col
			else :
				print('Turn: %s' %self.turn)
				print('The button %s (%s,%s) is already pressed' %(self.buttons[button]["id"],row,col))

		#button dictionnary with name and state {"button":{"id":int,"state":boolean}
		self.buttons={}
		for i in range(9):   
			#self.add_widget(Button(text=str(i),background_color=(1,1,1,1)))
			self.add_widget(Button(background_color=(1,1,1,1)))
			self.children[0].bind(on_press=callback)
			self.buttons[self.children[0]]={}
			self.buttons[self.children[0]]["id"]=i
			self.buttons[self.children[0]]["state"]=False
			print("dict",self.buttons)
			#print("children",self.children)


class MyApp(App):

    def build(self):
        return Table()


if __name__ == '__main__':
    MyApp().run()