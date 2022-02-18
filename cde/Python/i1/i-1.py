import os
from time import sleep
import pyautogui as py

inpp = input("How many photos are there?: ")
inpp = int(inpp)

        
def mainss():
    py.moveTo(2000, 500)
    py.rightClick()
    py.moveTo(2100, 550)
    sleep(1)
    py.click()
    sleep(2)
    py.hotkey("Enter")
    sleep(5)
    py.hotkey("Right")
    sleep(1)


for i in range(inpp):
        mainss()