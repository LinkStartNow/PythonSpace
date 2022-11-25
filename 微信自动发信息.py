# coding=gbk
import pyautogui
import time
from time import sleep
from datetime import datetime
import pyperclip

def end():
    pyautogui.press('win')
    time.sleep(0.5)
    p1 = pyautogui.locateCenterOnScreen(r'f:\img\switch.png', confidence=0.7)
    time.sleep(0.5)
    pyautogui.click(p1, duration=0.5)
    p2 = pyautogui.locateCenterOnScreen(r'f:\img\sleep.png', confidence=0.7)
    # pyautogui.moveTo(p2[0], p2[1] - 55, duration=0.5)
    pyautogui.click(p2[0], p2[1] - 55, duration=0.5)
    pyautogui.click()

def get_time():
    return str(datetime.now()).split()[1].split(':')[:2]

def open(x):
    pyautogui.hotkey('win', 'd')
    pyautogui.hotkey('ctrl', 'alt', 'w')
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy(x)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)

def send(x):
    pyperclip.copy(x)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

# end()
t = get_time()
if t[0] == '16':
    if t[1] == '00':
        open('董')
        send('下午好')
elif t[0] == '22':
    open('董')
    send('晚安')