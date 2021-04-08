from tkinter import Tk
import pyautogui

# Temp modules
import keyboard

class TransparentSelectionBox:
    def __init__(self, position: tuple, selection_area_color = "#1f80ff", overrideredirect=True):
        x, y = position
        
        self.root = Tk()
        if overrideredirect:
            self.root.overrideredirect(1)
        
        self.root.configure(bg=selection_area_color)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.4)
        
        self.root.bind('<Button-1>', self.close)
        
        self.startX = x
        self.startY = y
        
        self.above = False
        self.outside = False
        
        self.x = x
        self.y = y
        
        self.geometry(x, y, 100, 100)
        
        self.xOffset = 1
        self.yOffset = 1
        
        self.running = True
    
    def close(self, event):
        self.running = False
    
    def position(self):
        return (self.root.winfo_x(), self.root.winfo_y())
        
    
    def geometry(self, x, y, width, height):
        self.width = width
        self.height = height
        
        if x < 0:
            x = f'-{x}'
        else:
            x = f'+{x}'
        if y < 0:
            y = f'-{y}'
        else:
            y = f'+{y}'
            
        self.root.geometry('{}x{}{}{}'.format(width, height, x, y))
    
    def run(self):
        while self.running:
            mouseX, mouseY = pyautogui.position()
            self.rootX, self.rootY = self.position()
            
            if self.above:
                mouseY -= self.yOffset
            else:
                mouseY += self.yOffset
            if self.outside:
                mouseX -= self.xOffset
            else:
                mouseX += self.xOffset
            
            mouseX += 1
            mouseY += 1
            
            # print(self.rootY - self.height, mouseY)
            if mouseY < self.startY:
                self.above = True
            else:
                self.above = False
            if mouseX < self.startX:
                self.outside = True
            else:
                self.outside = False              
            
            if mouseX > self.rootX and not self.outside:
                width = mouseX - self.rootX
            else: 
                self.x += (mouseX - self.rootX)
                width = self.startX - self.x
                self.outside = True
            if mouseY > self.rootY and not self.above:
                height = mouseY - self.rootY
            else:
                self.y += (mouseY - self.rootY)
                height = self.startY - self.y        
            
            self.geometry(self.x, self.y, width, height)
            
            self.root.update()
            
            if keyboard.is_pressed('esc'):
                self.running = False
        
        x, y = self.position()
        
        self.root.destroy()
        
        return (x, y, self.width, self.height)
    
from mouse_controller import MouseController

mc = MouseController    

if __name__ == '__main__':
    print(TransparentSelectionBox(mc.position(), selection_area_color="#000000").run())