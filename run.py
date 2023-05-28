# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import config # file containing the API key
import os
from requests import get
os.system("clear")

""" ANSI color codes """
COLORS = {\
    "black": "\033[0;30m",
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "brown": "\033[0;33m",
    "blue": "\033[0;34m",
    "purple": "\033[0;35m",
    "cyan": "\033[0;36m",
    "cyan-background": "\u001b[46m",
    "black_background": "\u001b[40m",
}

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
    f = open("title_art.txt","r")
    ascii = "".join(f.readlines())
    title_tag = colorRep(ascii)
    print(title_tag)


def main():
    """
    Starts the application
    """
    print_art()
    
    print("Welcome to currency converter...\n")
    print("What will you like to do today?\n")
    start_app()


    #username = checkName()
        




main()