from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty
from random import randint

import colorsys
import time
import random

Builder.load_file('project1.kv')

class BackgroundRectangle(Widget):

    r = NumericProperty(0)

    def __init__(s, **kwargs):
         s.r = 0
         super(BackgroundRectangle, s).__init__(**kwargs)

    def on_touch_down(s, touch):
        if s.collide_point(touch.x,touch.y):
            s.r = 0.4

    def displayText(s):
        print('this is text')

class BackgroundCircle(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)
    hr = NumericProperty(0)
    
    def __init__(s, **kwargs):
        super(BackgroundCircle, s).__init__(**kwargs)

    def updateColor(self, *args):
        #self.hr = random.randint(65,120)
        self.hr+= 1
        color = colorsys.hsv_to_rgb((self.hr + 20)/200,1.0,1.0)
        print(color)
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

         

class BackgroundApp(App):

    def build(self):
        parent = Widget()
        rect = BackgroundRectangle()
        parent.add_widget(rect)
        #circle = BackgroundCircle()
        #parent.add_widget(circle)
        #Clock.schedule_interval(circle.updateColor, 1.0 / 2)
        return parent
        


if __name__ == '__main__':
    BackgroundApp().run()
