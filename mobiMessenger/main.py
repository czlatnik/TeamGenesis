'''This is going to be my starting point for the project I'm working on for the
semester. This program will subscribe to the MoBI program

'''
from mobiMessenger import messenger

m = messenger.mobiMessenger()
print(m.pullData("Polar H7 919CB51C/s1/char1"))
