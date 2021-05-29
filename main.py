from transparent_selection_box import TransparentSelectionBox
import keyboard
import pyautogui
import cv2
import pytesseract
import clipboard
from mouse_controller import MouseController
import time
import platform

class NotCompatibleWithOS(Exception):
    pass

OS = platform.system().lower()

if OS == "windows":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
elif OS == "darwin":
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
elif OS == "linux":
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
else:
    raise NotCompatibleWithOS(f"This program is not compatible with {OS}")
    
mc = MouseController

pressed = False

while True:
    if keyboard.is_pressed('ctrl+alt+p'):
        while True:
            if mc.state(mc.LEFT):
                x, y, width, height = TransparentSelectionBox(mc.position()).run()
                
                pyautogui.screenshot('screenshot.png', region=(x, y, width, height))
                img = cv2.imread('screenshot.png')
                text = pytesseract.image_to_string(img).replace('', '')
                clipboard.copy(text)
                print(text)
                break
            
            pressed = True
    if mc.state(mc.RIGHT):
        print('exit')
        break
