import sys
import time
import os

os.system("clear")

""" ANSI color codes """
COLORS = {\
    "black": "\033[0;30m",
    "red": "\033[0;31m",
    "green": "\033[32m",
    "blue": "\u001b[34;1m",
    "white": "\u001b[37m",
    "black_background": "\u001b[40m",
    "red_background": "\033[41m",
    "cyan_background": "\u001b[46;1m",
    "stop_color" : "\x1b[0m",
}


def typewriter(message):
    """
    Writes the message in a typewriter format where used
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.075)
        else:
            time.sleep(1)

def clear_screen():
    """
    Clears the screen when used
    """
    os.system("clear")


def colorRep(text):
    """
    Coordinate color rendering 
    """
    for color in COLORS:
        text = text.replace("[[" + color + "]]",COLORS[color])
    return text


def print_art():
    """
    Open the file and print out the art onto the terminal
    """
    with open("title_art.txt") as r:
        while f := r.readlines():
            ascii = "".join(f)
            title_tag = colorRep(ascii)
            print(title_tag)