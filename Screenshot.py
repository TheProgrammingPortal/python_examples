# Method - 1 --> using pyautogui module

import pyautogui, time
time.sleep(5)
screeshot = pyautogui.screenshot()
screeshot.save('image1.png')
print('screenshot taken using pyautogui.')

# Method - 2 --> using Pillow module

from PIL import ImageGrab
image = ImageGrab.grab(bbox=(100,100,500,800))
image.save('image2.png')
print('screenshot taken using Pillow.')

