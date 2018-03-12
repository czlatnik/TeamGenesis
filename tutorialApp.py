from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty
from random import randint

import colorsys
import time
import random

from kivy.properties import StringProperty

from kivy.uix.screenmanager import ScreenManager, Screen

class TutorialApp(App):
    userName = StringProperty('None')
    hr = NumericProperty(55)

    def build(self):
        Builder.load_file('tutorialApp.kv')
        sm = ScreenManager()
        sm.add_widget(startScreen(name='start'))
        sm.add_widget(hrScreen(name='hrScreen'))
        #circle = BackgroundCircle()
        #hrScreen.add_widget(circle)
        
        return sm

class startScreen(Screen):
    pass
##    def displayText(self, name2, *args):
##        self.userName = name2
##        print(self.userName)
##    

class hrScreen(Screen):

    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super(hrScreen, self).__init__(**kwargs)
##        self.circle = BackgroundCircle()
##        self.add_widget(self.circle)
        Clock.schedule_interval(self.updateColor, 1.0 / 2)
        #potentially an issue bc after instantiation, it won't stop updating
    
    def getName(self, *args):
        return userName.get

    def updateColor(self, *args):
        #self.hr = random.randint(65,120)
        App.get_running_app().hr+= 1
        color = colorsys.hsv_to_rgb((App.get_running_app().hr + 20)/200,1.0,1.0)
        #print(color)
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
    
    pass

if __name__ == "__main__":
    TutorialApp().run()
