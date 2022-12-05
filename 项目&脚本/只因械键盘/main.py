import keyboard
from threading import Thread
from playsound import playsound

def play(x):
    playsound(x + '.mp3')

def yyds(x):
    if x.event_type == 'down':
        match x.name:
            case 'j':
                Thread(target=play, args='j').start()
            case 'n':
                Thread(target=play, args='n').start()
            case 't':
                Thread(target=play, args='t').start()
            case 'm':
                Thread(target=play, args='m').start()
            case 'b':
                Thread(target=play, args='b').start()

keyboard.hook(yyds)
keyboard.wait('esc')