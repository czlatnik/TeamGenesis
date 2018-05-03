from kivy.config import Config

Config.set('graphics', 'width', '1440')
Config.set('graphics', 'height', '250')
Config.set('graphics', 'resizable', '1') #0 being off 1 being on as in true/false
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'top', '0') 
Config.set('graphics', 'left', '0')
Config.set('graphics','borderless','0') #hit esc to exit window

from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.properties import NumericProperty, ObjectProperty, StringProperty,\
                            BooleanProperty, ReferenceListProperty, BoundedNumericProperty,\
                            ListProperty
from random import randint

import colorsys
import time
import random
import math

from datetime import timedelta

class projectApp(App):
    
    #Variables that can be accessed throughout the app
    start_time = NumericProperty(time.time())
    stopwatch = StringProperty('0')
    progressvalue = NumericProperty(0)
    countdown = BooleanProperty(False)
    hr = NumericProperty(55)
    age = NumericProperty(35) #get from OnePortal
    skinTemp = NumericProperty(96)
    skinTempText = StringProperty(' \xb0F')
    backgroundSource = StringProperty('img/blackBackground.png')
    oceanBackgroundSource = StringProperty('img/ocean1.jpg')
    hillCaption = StringProperty('Hello, space traveler!') #changes with info from OnePortal


    def build(self):
        Builder.load_file('projectApp.kv')
        sm = ScreenManager(transition=NoTransition())
        profScreen = profileScreen(name = 'profile')
        setScreen = settingsScreen(name = 'settings')
        swimScreen = scubaScreen(name = 'scuba')
        sm.add_widget(profScreen)
        sm.add_widget(setScreen)
        sm.add_widget(swimScreen)
        return sm


## Screens
class profileScreen(Screen):

    def __init__(self, **kwargs):
        super(profileScreen, self).__init__(**kwargs)

    def on_touch_point(self, touch):
        if self.ids.my_image.collide_point(*touch.pos):
            self.imageClicked = True
        else:
            self.imageClicked = False
            
class settingsScreen(Screen):

    def __init__(self, **kwargs):
        super(settingsScreen, self).__init__(**kwargs)

class scubaScreen(Screen):
    
    def __init__(self, **kwargs):
        super(scubaScreen, self).__init__(**kwargs)


## Widgets
class SettingsButtonWidget(Widget):

    imageClicked1 = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(SettingsButtonWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.ids.setWidgetID.collide_point(*touch.pos):
            self.imageClicked1 = True
        else:
            self.imageClicked1 = False

class FishButtonWidget(Widget):

    imageClicked2 = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(FishButtonWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.ids.fishWidgetID.collide_point(*touch.pos):
            self.imageClicked2 = True
        else:
            self.imageClicked2 = False

class BackArrowWidget(Widget):
    imageClicked3 = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(BackArrowWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.ids.backArrowWidgetID.collide_point(*touch.pos):
            self.imageClicked3 = True
        else:
            self.imageClicked3 = False

class HRWidget(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)
    labelColor = ListProperty([0,1,1,1])

    def __init__(self, **kwargs):
        super(HRWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.updateColor, 1.0 / 5)

    def updateColor(self, *args):
        App.get_running_app().hr += 1
        color = colorsys.hsv_to_rgb((App.get_running_app().hr + 20)/200,1.0,1.0)
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

        if App.get_running_app().hr > 0.85 * (220 - App.get_running_app().age):
            App.get_running_app().backgroundSource = 'img/redBackground.png'
            self.labelColor = [1,0,0,1]

            if App.get_running_app().hr > 200:
                App.get_running_app().hr = 55
            
        else:
            App.get_running_app().backgroundSource = 'img/blackBackground.png'
            self.labelColor = [1,1,1,1]

class SkinTempWidget(Widget):

    def __init__(self, **kwargs):
        super(SkinTempWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.updateTemp, 1.0)

    #update skintemp based on Empatica data

    def updateTemp(self, *args):
        temp = App.get_running_app().skinTemp

        temp += 1
        if App.get_running_app().skinTempText == ' \xb0F':

            if (temp > 100) or (temp < 50):
                temp = 80
        else: #celcius
            if temp > 40:
                temp = (temp - 32) * 5/9
            if (temp > 40) or (temp < 20):
                temp = 35
            
        App.get_running_app().skinTemp = math.ceil(temp)
             
class Knob(Widget):

    min = NumericProperty(0)
    max = NumericProperty(100)
    range = ReferenceListProperty(min, max)
    value = NumericProperty(0)
    step = BoundedNumericProperty(1, min=0)
    curve = BoundedNumericProperty(1, min=1)
    knobimg_source = StringProperty("")
    knobimg_color = ListProperty([1, 1, 1, 1])
    knobimg_size = BoundedNumericProperty(0.9, max=1.0, min=0.1)
    show_marker = BooleanProperty(True)
    marker_img = StringProperty("")
    marker_color = ListProperty([1, 1, 1, 1])
    knobimg_bgcolor = ListProperty([0, 0, 0, 1])
    markeroff_img = StringProperty("")
    markeroff_color = ListProperty([0, 0, 0, 0])
    marker_startangle = NumericProperty(0)
    marker_ahead = NumericProperty(0)

    _angle          = NumericProperty(0)            # Internal angle calculated from value.
    _angle_step     = NumericProperty(0)            # Internal angle_step calculated from step.

    def __init__(self, *args, **kwargs):
        super(Knob, self).__init__(*args, **kwargs)
        self.bind(show_marker   =   self._show_marker)
        self.bind(value         =   self._value)
        Clock.schedule_interval(self.updateTime, 1.0/1000) #updates time/value

    def updateTime(self, *args):
        elapsed_time = time.time() - App.get_running_app().start_time

        #Changing background ocean view
        App.get_running_app().oceanBackgroundSource = 'img/ocean' + str(math.ceil(elapsed_time / 100 * 20 )% 21) + '.jpg' 
        
        progress = elapsed_time / 2400 * 100 
        if App.get_running_app().countdown == True:
            elapsed_time = 2400 - elapsed_time
            if elapsed_time < 0:
                elapsed_time = 0
            progress = 100 - progress
            if progress < 0:
                progress = 0
        App.get_running_app().progressvalue = elapsed_time / 2400 * 100 #set for 40 min timespan
        App.get_running_app().stopwatch = str(timedelta(seconds=elapsed_time)).split(".")[0]

    def _value(self, instance, value):
        self._angle     =   pow( (value - self.min)/(self.max - self.min), 1./self.curve) * 360.
        self.on_knob(value)

    def _show_marker(self, instance, flag):
        # "show/hide" marker.
        if flag:
            self.knobimg_bgcolor[3] = 1
            self.marker_color[3] = 1
            self.markeroff_color[3] = 1
        else:
            self.knobimg_bgcolor[3] = 0
            self.marker_color[3] = 0
            self.markeroff_color[3] = 0

    def update_angle(self, touch):
        posx, posy          =   touch.pos
        cx, cy              =   self.center
        rx, ry              =   posx - cx, posy - cy

        if ry >= 0:                                 # Quadrants are clockwise.
            quadrant = 1 if rx >= 0 else 4
        else:
            quadrant = 3 if rx <= 0 else 2
        try:
            angle = math.atan(rx / ry) * (180./math.pi)
            if quadrant == 2 or quadrant == 3:
                angle = 180 + angle
            elif quadrant == 4:
                angle = 360 + angle

        except:                                   # atan not def for angle 90 and 270
            angle = 90 if quadrant <= 2 else 270

        self._angle_step    =   (self.step*360)/(self.max - self.min)
        self._angle         =   self._angle_step
        while self._angle < angle:
            self._angle     =   self._angle + self._angle_step

        relativeValue   =   pow((angle/360.), 1./self.curve)
        self.value      =   (relativeValue * (self.max - self.min)) + self.min


    #TO OVERRIDE
    def on_knob(self, value):
        pass #Knob values listenerr
       

if __name__ == '__main__':
    projectApp().run()
