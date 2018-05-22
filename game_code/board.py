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
		self.cols=3
		self.size_hint=(0.7,0.7)
		self.pos_hint={"center_x":0.5,"center_y":0.5}
		
		#This returns the row and column of the button presssed
		def callback(button):
			#print(instance,button)
			for i in range(9):
				if button == self.buttons['button%s' %i]:
					row=i//self.cols
					col=i%self.cols
					#print("row",row,"col",col)
			print('The button %s (%s,%s) is being pressed' %(button.text,row,col))
			return row,col

		#button dictionnary with name 
		self.buttons={}
		for i in range(9):   
			self.add_widget(Button(text=str(i)))
			self.buttons["button%s" %i]=self.children[0]
			self.buttons["button%s" %i].bind(on_press=callback)
			#print("dict",self.buttons)
			#print("children",self.children)


class MyApp(App):

    def build(self):
        return Table()


if __name__ == '__main__':
    MyApp().run()