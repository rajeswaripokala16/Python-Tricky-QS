import random
import pyautogui as pg
import time

animal = ('monkey', 'donkey', 'dog')

time.sleep(8)  # Wait 8 seconds so you can open WhatsApp Web

for i in range(500):
    a = random.choice(animal)
    pg.write("You are a " + a)
    pg.press('enter')

You are a monkey
You are a monkey
You are a dog
You are a dog
You are a monkey
You are a monkey
You are a dogYou are a dog
You are a donkey
You are a dog
You are a monkey
You are a monkey
You are a donkey
You are a donkey
You are a donkey
You are a monkey
You are a donkey
You are a donkey

You are a donkey
You are a dog
You are a dog
