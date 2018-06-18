import kivy
#kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.graphics import Color,Ellipse
from kivy.graphics.transformation import Matrix

import os
import paramiko

### Configuration of the TUIO input 
Config.set('input','Reactable','tuio,127.0.0.1:3333')


class Table(FloatLayout):

	def __init__(self, **kwargs):

		super(Table, self).__init__(**kwargs)
		
		### Where to launch the app on the screen
		width=1280
		height=800
		Window.top = 0
		Window.left = width	
		Window.size= (width,height)

		self.pos_hint={"center_x":0.5,"center_y":0.5}
		
		Window.clearcolor = (1,1, 1, 0)

		self.turn = 0
		self.cols = 3

		### This function will be called everytime something is tracked on the Reactable
		###	Here we define what to do if it's a fludical
		def on_motion(self, etype, motionevent):
			
			### We care only about flucidal
			#print(motionevent.pos)
			if 'markerid' in motionevent.profile:
				### We apply the transformation
				a=0.875
				dy=15

				mx,my=a*motionevent.pos[0],motionevent.pos[1]+dy

				### Here we draw a green point where the flucidal is
				with self.canvas:
					Color(0,1,0)
					d=3.
					Ellipse(pos=(mx-d /2,my-d/2),size=(d,d))

				

				### We find the button pressed and make the play
				### Check if it's the relaunch button
				if mx>=514 and mx<=576 and my>=602 and my<=678:
					relaunch()
					pass

				### Check a play button
				#print(mx,my)
				for x in range(3):
					if mx>=(316+x*160) and mx<=(454+x*160):
						for y in range(3):
							if my>=(430-y*114) and my<=(530-y*114):

								id_button = y*self.children[0].cols + x

								for button in self.children[0].buttons:
									if self.children[0].buttons[button]["id"] == id_button :
										b = button
								### We make the play
								play(b)
		pass

		Window.bind(on_motion=on_motion)

		### This returns the row and column of the button presssed if not already pressed
		def play(button):

			### We get the id, row and column of the button pressed
			i = self.buttons[button]["id"]
			col=(i)//self.cols
			row=(i)%self.cols 

			### We change color and return row,col if the button isn't already pressed
			if not(self.buttons[button]["state"]):
				if not(self.turn%2):
					button.background_color=(128,0,0,1)
				else:
					button.background_color=(0,0,128,1)
				self.turn+=1
				self.buttons[button]["state"]=True
				print('Turn: %s' %self.turn)
				print('The button %s (%s,%s) is being pressed' %(self.buttons[button]["id"],row,col))
				f = open('data', 'w')
				f.write(str(self.turn)+'\n')
				f.write(str(row)+'\n')
				f.write(str(col)+'\n')
				f.close()
				ssh = paramiko.SSHClient()
				ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
				ssh.connect("10.77.3.120", username="poppy", password="poppy")
				sftp = ssh.open_sftp()
				sftp.put("data", "/home/pi/poppy_project/game_code/data")
				sftp.close()
				ssh.close()


			else :
				#print('Turn: %s' %self.turn)
				#print('The button %s (%s,%s) is already pressed' %(self.buttons[button]["id"],row,col))
				pass

		### This is to relaunch the game (make sure there is no more button on play)
		def relaunch():
			self.turn=0
			for but in self.buttons:
				self.buttons[but]["state"]=False
				but.background_color=(1,1,1,1)
			f = open('data', 'w')
			f.write(str(-1)+'\n')
			f.write(str(0)+'\n')
			f.write(str(01)+'\n')
			f.close()
			ssh = paramiko.SSHClient()
			ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
			ssh.connect("10.77.3.120", username="poppy", password="poppy")
			sftp = ssh.open_sftp()
			sftp.put("data", "/home/pi/poppy_project/game_code/data")
			sftp.close()
			ssh.close()
			pass


		### We add the buttons on the board
		### button dictionnary with name and state {button:{"id":int,"state":boolean}}		

		self.buttons={}

		self.add_widget(Button(background_color=(1,1,1,1),pos_hint={"center_x":0.425,"center_y":0.8},size_hint=(0.05,0.1)))
		self.buttons[self.children[0]]={}
		self.buttons[self.children[0]]["id"] = -1
		self.buttons[self.children[0]]["state"] = False

		buttonsNumber = 9
		for i in range(buttonsNumber):
			col=(i)//self.cols
			row=(i)%self.cols  
			x,y= (0.3+float(row)/8),(0.60-float(col)/7)
			
			self.add_widget(Button(background_color=(1,1,1,1),pos_hint={"center_x":x,"center_y":y},size_hint=(0.11,0.13)))
			self.do_layout()
			
			#self.children[0].bind(on_press=play)
			self.buttons[self.children[0]] = {}	
			self.buttons[self.children[0]]["id"] = i
			self.buttons[self.children[0]]["state"] = False


class MyApp(App):

    def build(self):
        return Table()

if __name__ == '__main__':
    MyApp().run()
