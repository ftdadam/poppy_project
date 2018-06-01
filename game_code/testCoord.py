import kivy
#kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

#Configuration de l'input TUIO
Config.set('input','Reactable','tuio,127.0.0.1:3333')

class Foo(FloatLayout):
  # stupid child class so we can print when we get touch events
  def on_touch_down(self, t):
  	print(t.spos)
  	tx,ty=t.spos[0],t.spos[1] 
	if self.collide_point(*t.pos):
		if tx>=0.4 and tx<=0.7 and ty>=0.5 and ty<=0.7:
			print t


class Table(FloatLayout):
	def __init__(self, **kwargs):
		super(Table, self).__init__(**kwargs)
		self.turn = 0



		#This returns the row and column of the button presssed if not already pressed
		
		def callback(button):
			#print(instance,button)
			i = self.buttons[button]["id"]
			#row=i//self.cols
			#col=i%self.cols
			#we change colors and return row,col if the button isn't already pressed
			
			if not(self.turn%2):
				button.background_color=(128,0,0,1)
			else:
				button.background_color=(0,0,128,1)
			self.turn+=1
			self.buttons[button]["state"]=True
			print('Turn: %s' %self.turn)
			print('The button %s (%s,%s) is being pressed' %(self.buttons[button]["id"],2,2))
			return 2,3


		"""
			else :
				print('Turn: %s' %self.turn)
				print('The button %s (%s,%s) is already pressed' %(self.buttons[button]["id"],row,col))
		"""
		self.add_widget(Foo(size_hint=(1, 1)))

		#button dictionnary with name and state {"button":{"id":int,"state":boolean}
		self.buttons={}
		for i in range(4):   
			#self.add_widget(Button(text=str(i),background_color=(1,1,1,1)))
			self.add_widget(Button(background_color=(1,1,1,1),pos=(300*i,0),size_hint=(0.2,0.2)))
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