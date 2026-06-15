import random
import pyautogui as pg
import time

animal = ('Rowdy Girl','Cement','Thikka dhaana','Bhaaa');

time.sleep(8)  # Wait 8 seconds so you can open WhatsApp Web

for i in range(16):
    a = random.choice(animal)
    pg.write("choodu mey  " + a)
    pg.press('enter')
