import subprocess
import pyautogui
import win32gui
import win32con
import os

def callback(hwnd, windows):
    if win32gui.IsWindowVisible(hwnd):
        windows.append(hwnd)

windows = []

win32gui.EnumWindows(callback, windows)

for window in windows:
    win32gui.ShowWindow(window, win32con.SW_HIDE)

for window in windows:
    win32gui.ShowWindow(window, win32con.SW_SHOW)

filePath = "screen.png"
img = pyautogui.screenshot()
img.save(filePath)

subprocess.run(["wal", "-i", filePath], shell=True)

for path in os.listdir():
    if (".json" in path):
        os.remove(path)

os.remove(filePath)
