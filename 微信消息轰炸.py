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

name = input('�Է�����΢���еı�ע:')
times = int(input('���ʹ�����'))
msg = input('�������ݣ�')
open(name)
while times != 0:
    times -= 1
    send(msg)
