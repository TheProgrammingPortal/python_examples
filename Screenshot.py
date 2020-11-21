# import pyautogui, time
# time.sleep(5)
# screeshot = pyautogui.screenshot()
# screeshot.save('image1.png')
# print('screenshot taken.')
#

from PIL import ImageGrab
image = ImageGrab.grab(bbox=(100,100,500,800))
image.save('image2.png')

