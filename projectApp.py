from kivy.app import App
from kivy.lang import Builder

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.vector import Vector

from random import randint

import colorsys
import time
import random

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors.button import ButtonBehavior


class projectApp(App):

    hr = NumericProperty(55)
    widgetNum = NumericProperty(0)
    stat1 = StringProperty('Heart Rate')
    stat2 = StringProperty('Tidal Volume')
    stat3 = StringProperty('Blood Pressure')
    stat4 = StringProperty('Breathing Rate')

    def build(self):
        Builder.load_file('projectApp.kv')
        sm = ScreenManager()
        sm.add_widget(startScreen(name='start'))
        sm.add_widget(profileScreen(name='profile'))

        return sm

class chooseDataScreen(Screen):
    pass

class startScreen(Screen):
    pass

class profileScreen(Screen):

    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)

    def __init__(self, **kwargs):
        super(profileScreen, self).__init__(**kwargs)

        Clock.schedule_interval(self.updateColor, 1.0 / 2)

    def updateColor(self, *args):
        App.get_running_app().hr+= 1
        color = colorsys.hsv_to_rgb((App.get_running_app().hr + 20)/200,1.0,1.0)
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

if __name__ == '__main__':
     projectApp().run()
