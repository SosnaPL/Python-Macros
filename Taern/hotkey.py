import threading, os
from pynput import keyboard
from pynput.mouse import Controller, Button
import ctypes
import binascii

MessageBox = ctypes.windll.user32.MessageBoxW

hotkeys = {}
listener_thread = None

mouse = Controller()

def add_hotkey(key, callback):
    hotkeys[key] = callback

def on_press(key):
    key = key.char if hasattr(key, "char") else key.name
    if key in hotkeys:
        t = threading.Thread(target=hotkeys[key])
        t.daemon = True
        t.start()

def exitapp():
    listener_thread.stop()
    os._exit(0)
    
def run():
    listener_thread.join()
    
def msg_box(message, title):
    MessageBox(None, title, message, 0)
    
def to_rgb(RGBint):
    red =   RGBint & 255
    green = (RGBint >> 8) & 255
    blue =   (RGBint >> 16) & 255
    return "#"+hex(red)[2:].zfill(2)+hex(green)[2:].zfill(2)+hex(blue)[2:].zfill(2)
    
def pixel_get_color(x, y):
    hdc = ctypes.windll.user32.GetDC(0)
    return to_rgb(ctypes.windll.gdi32.GetPixel(hdc, x, y))
    
def click(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left)
def mouse_move(x, y):
    mouse.position = (x, y)

listener_thread = keyboard.Listener(on_press=on_press)
listener_thread.start()