import kivy
#kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.graphics import Color,Line
from kivy.graphics.transformation import Matrix

#Configuration de l'input TUIO
Config.set('input','Reactable','tuio,127.0.0.1:3334')

#
Config.set('graphics','position','custom')
Config.set('graphics','top','0')
Config.set('graphics','left','1440')

class Foo(FloatLayout):
	# stupid class so we can print when we get touch events

		def on_touch_down(self, t,**kwargs):
		  	#t.spos[0]=t.spos[0]-0.2
		  	#t.spos[1]=t.spos[1]-0.2
		  	#print("Touch")
		  	#print(t)
		  	t.x=t.x-0
		  	#print(t)

			if self.collide_point(*t.pos):
				if ((t.x-(center_x))**2 +(t.y-(center_y))**2)<=r**2:
					with self.canvas:
						Color(1,0,0)
						d=2.
						Line(ellipse=(t.x-d /2,t.y-d/2,d,d))
				else :
					with self.canvas:
						Color(0.2,0.2,0.2)
						d=2.
						Line(ellipse=(t.x-d /2,t.y-d/2,d,d))



class Table(FloatLayout):

	


	def callback(button):
			#print(instance,button)
			i = self.buttons[button]["id"]
			col=(i)//self.cols
			row=(i)%self.cols 
			#we change colors and return row,col if the button isn't already pressed
			
			if not(self.turn%2):
				button.background_color=(128,0,0,1)
			else:
				button.background_color=(0,0,128,1)
			self.turn+=1
			self.buttons[button]["state"]=True
			print('Turn: %s' %self.turn)
			print('The button %s (%s,%s) is being pressed' %(self.buttons[button]["id"],row,col))
			return row,col

			"""
			else :
				print('Turn: %s' %self.turn)
				print('The button %s (%s,%s) is already pressed' %(self.buttons[button]["id"],row,col))
			"""




	def __init__(self, **kwargs):


		def on_motion(self, etype, motionevent):
			print (motionevent.pos)
			motionevent.pos=(300,300)
			print (motionevent.pos)
		pass
		
		super(Table, self).__init__(**kwargs)

		width=1280
		height=800
		Window.top = 0
		Window.left = 0	
		Window.size= (width,height)

		Window.clearcolor = (1,1, 1, 0)

		Window.bind(on_motion=on_motion)

		self.size=Window.size
		self.pos_hint={"center_x":0.5,"center_y":0.5}

		self.r=300
		self.dx = -50
		self.dy = 0

		global r
		global center_x
		global center_y

		r=self.r
		center_x=self.center_x+self.dx
		center_y=self.center_y+self.dy

		#print(self.center_x,self.center_y)
		with self.canvas:
			Color(1,0,0)
			Line(circle=(self.center_x+self.dx,self.center_y+self.dy,self.r))
			Color(0,1,0)
			Line(ellipse=(200,0,880,800))
		
			
		self.add_widget(Foo(size_hint=(1, 1)))
		"""
		#button dictionnary with name and state {"button":{"id":int,"state":boolean}
		self.buttons={}
		buttonsNumber = 9
		for i in range(buttonsNumber):
			col=(i)//self.cols
			row=(i)%self.cols  
			x,y= (0.3+float(row)/7),(0.65-float(col)/7)
			self.add_widget(Button(background_color=(1,1,1,1),pos_hint={"center_x":x,"center_y":y},size_hint=(0.11,0.13)))
			self.children[0].bind(on_press=callback)
			self.buttons[self.children[0]]={}
			self.buttons[self.children[0]]["id"]=i
			self.buttons[self.children[0]]["state"]=False
			#print("dict",self.buttons)
			#print("children",self.children)
		"""




class MyApp(App):

    def build(self):
        return Table()



if __name__ == '__main__':
    MyApp().run()