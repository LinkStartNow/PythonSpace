# coding=gbk
import pyautogui
from time import sleep
from datetime import datetime
import pyperclip

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

name = input('对方在你微信中的备注:')
times = int(input('发送次数：'))
msg = input('发送内容：')
open(name)
while times != 0:
    times -= 1
    send(msg)
