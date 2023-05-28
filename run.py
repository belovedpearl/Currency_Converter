# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import config # file containing the API key
import os
from requests import get
os.system("clear")

# URL for the get request
BASE_URL = "https://free.currconv.com/"
key = config.API_KEY


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
def get_currencies():
    """
    Connect the base url and the currency link
    Get the json file
    list the values found in the returned 
    """
    # list of currencies provided in the API documentation
    currency_link = f"api/v7/currencies?apiKey={key}"
    url = BASE_URL + currency_link
    # Send a get request to the base url
    # Access the result key in the json file
    data = get(url).json()['results']
    # Convert the returned values to a list
    data = list(data.items())
    data.sort()

    return data 


def start_app():
    currencies = get_currencies() 
    print("Press 1 to list the available currencies.\n")
    print("Press 2 to convert from one currency to another\n")
    print("Press 3 to get exchange rate of two currencies.\n\n")
    while True:
        answer = input("Choose an option or press q to quit.")

        if answer == "q":
            break
        elif answer == "1":
            list_currencies(currencies)
        elif answer == "2":
            currency1 = input("Enter your base currency id.").upper()
            currency2 = input("What currency id are you converting to?").upper()
            amount = input(f"Enter an amount in {currency1}.").upper()
            convert_currencies(currency1, currency2, amount)
        elif answer == "3":
            currency1 = input("Enter a base currency id.").upper()
            currency2 = input("Enter the next currency id").upper()
            exchange_rate(currency1, currency2)
        else:
            print("You have made an invalid choice.")


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