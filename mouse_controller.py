import win32gui
import win32api

# Quicker and lower level access to the mouse

class MouseController:
    LEFT = 0x01
    RIGHT = 0x02
    
    def position():
        flags, hcursor, (x, y) = win32gui.GetCursorInfo()
        return (x, y)
    
    def state(button: hex):
        print(win32api.GetKeyState(button))
        if win32api.GetKeyState(button) < 0:
            return True
        else: 
            return False