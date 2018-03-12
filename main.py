from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty

from random import randint
import zmq
import sys
import BtPacket_pb2
import colorsys
import time
import random

Builder.load_file('backgroundChange.kv')

class HeartRateMeasurement(object):
    host = "192.168.0.101"
    context = zmq.Context()
    subSocket = context.socket(zmq.SUB)
    subSocket.connect("tcp://%s:5556" % host)
    subSocket.setsockopt_string(zmq.SUBSCRIBE, "")
    topicName = "Polar H7 919CB51C/Heart Rate/Heart Rate Measurement"

#call this method to get the rate as passed from MoBI
    @classmethod
    def getHR(cls):
        rate = 0
        try:
            while True:
                try:
                    packetString = cls.subSocket.recv(zmq.NOBLOCK)
                except zmq.ZMQError:
                    return rate
                btPacket = BtPacket_pb2.BtPacket()
                btPacket.ParseFromString(packetString)
                if btPacket.topicName == cls.topicName:
                    data = btPacket.data
                    rate = int(data[2:4], 16)
                    print(" heart rate: %d" % rate)

        except KeyboardInterrupt:
            exit(0)
        return rate

class BackgroundRectangle(Widget):

    r = NumericProperty(0)

    def __init__(s, **kwargs):
         s.r = 0
         super(BackgroundChange, s).__init__(**kwargs)
    
    def create(self, hrm = HeartRateMeasurement()):
         self.hrm = hrm

    def getHR(self):
         return self.hrm.getHR()
        
    def update(self, *args):
         self.r = self.getHR()/100
         #print(hr)

    def on_touch_down(s, touch):
        if s.collide_point(touch.x,touch.y):
            s.r = 0.4

class BackgroundCircle(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)
    hr = NumericProperty(65)
    
    def __init__(s, **kwargs):
        super(BackgroundCircle, s).__init__(**kwargs)

    def create(self, hrm = HeartRateMeasurement()):
        self.hrm = hrm

    def getHR(self):
        return self.hrm.getHR()

    def updateColor(self, *args):
        #self.hr = random.randint(65,120)
        self.hr+= 1
        #self.hr = self.hrm.getHR()
        color = colorsys.hsv_to_rgb((self.hr + 20)/200,1.0,1.0)
        print(color)
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

         

class BackgroundApp(App):

    def build(self):
        parent = Widget()
        circle = BackgroundCircle()
        #circle.create()
        parent.add_widget(circle)
        Clock.schedule_interval(circle.updateColor, 1.0 / 10)
        return parent
        


if __name__ == '__main__':
    BackgroundApp().run()
