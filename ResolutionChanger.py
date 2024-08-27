import win32api
import win32con
import pywintypes


def InitializeResolution(Width, Height, Freq):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = Width
    devmode.PelsHeight = Height
    devmode.DisplayFrequency = Freq
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT | win32con.DM_DISPLAYFREQUENCY
    win32api.ChangeDisplaySettings(devmode, 0)

def ChooseResolution():
    Width = input("Choose a Width: ")
    match Width:
        case "default" | "d":
            InitializeResolution(Width=1920,Height=1080,Freq=170)
            exit()
        case "stretch" | "s":
            InitializeResolution(Width=1440,Height=1080,Freq=170)
            exit()
        case _:
            Width = int(Width)
            
        
    Height = int(input("Choose a Height: "))
    Freq = int(input("Choose a Refresh Rate: "))
    InitializeResolution(Width,Height,Freq)
    

ChooseResolution()
