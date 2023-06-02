# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import config  # file containing the API key
import os
from requests import get
from regulator import *
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("currency_converter")


# URL for the get request
BASE_URL = "https://free.currconv.com/"

# Get APIkey contained in the config file
KEY = config.API_KEY


def get_countries(currencies):
    """
    Gets the list of countries avialable in the url
    """
    # list of countries provided in the API documentation
    countries_link = (
        f"api/v7/countries?apiKey={KEY}"
    )
    url = BASE_URL + countries_link
    # Send a get request to the base url
    # Access the result key in the json file
    data_returned = get(url).json()["results"]
    # Convert the returned values to a list
    data_returned = list(data_returned.items())

    for data in data_returned:
        # Access the specific country name
        print(data[1]["name"])


def exchange_rate(currency1, currency2):
    """
    Return conversion rate
    Checks if a wrong entry was made
    """
    # Multiple query for the two currency conversion
    currency_convert_link = (
        f"api/v7/convert?q={currency1}_{currency2}&compact-ultra&apiKey={KEY}"
    )
    url = BASE_URL + currency_convert_link
    # Send a get request
    response = get(url)

    data = response.json()
    # Check for incorrect or unlisted currency
    if data["results"] == {}:
        print("Invalid currencies")
        return
    # Get the rate value into a list
    rate = list(data.values())[1][currency1 + "_" + currency2]["val"]
    print(f"Rate of {currency1} to {currency2}  = {rate}")
    return rate


def convert_currencies(currency1, currency2, amount):
    """
    Convert one currency to another
    Takes a specified amount in the base currency
    """
    rate = exchange_rate(currency1, currency2)
    # Check if returned rate is invalid
    if rate is None:
        return
    # Convert to number
    try:
        amount = float(amount)
    # In case of error
    except:
        print("Invalid amount")
        return
    converted_amount = rate * amount
    print(f"{amount}{currency1} is equal to {converted_amount:.2f}{currency2}")
    return converted_amount


def list_currencies(currencies):
    """
    List the returned currencies
    """
    typewriter(colorRep("Column 1 displays [[red]]IDENTITY[[black]] of currencies.\n"))
    typewriter(
        colorRep("Column 2 displays [[red]]NAMES[[black]] of currencies.\n")
    )
    typewriter(
        colorRep("Column 3 displays [[red]]SYMBOLS[[black]] of the currencies.\n")
    )

    # loop through the returned tuple
    for name, currency in currencies:
        name = currency["currencyName"]
        identity = currency["id"]
        # Get the symbol
        symbol = currency.get(
            "currencySymbol", ""
        )  # Return value if found and "" if not existing
        print(
            colorRep(f"[[blue]]{identity}[[black]] - {name} - [[red]]{symbol}[[black]]")
        )


def get_currencies():
    """
    Connect the base url and the currency link
    Get the json file
    list the values found in the returned
    """
    # list of currencies provided in the API documentation
    currency_link = f"api/v7/currencies?apiKey={KEY}"
    url = BASE_URL + currency_link
    # Send a get request to the base url
    # Access the result key in the json file
    data = get(url).json()["results"]
    # Convert the returned values to a list
    data = list(data.items())
    data.sort()

    return data


def start_app():
    """
    Prompts user to make a choice
    Continues the program in the path chosen
    """
    currencies = get_currencies()

    typewriter(
        colorRep(
            "Press [[red]]1[[black]] to [[red]]LIST[[black]] the available currencies.\n"
        )
    )
    typewriter(
        colorRep(
            "Press [[red]]2[[black]] to [[red]]CONVERT[[black]] from one currency to another.\n"
        )
    )
    typewriter(
        colorRep(
            "Press [[red]]3[[black]] to get [[red]]EXCHANGE[[black]] rate of two currencies.\n"
        )
    )
    typewriter(
        colorRep(
            "Press [[red]]4[[black]] to [[red]]GET[[black]] a list of available countries.\n\n"
        )
    )

    while True:
        answer = input(
            colorRep("Choose an option or press [[red]]q[[black]] to quit.\n")
        )

        if answer == "q":
            typewriter("Thank you for using MyCurrency...\n")
            typewriter(colorRep("[[blue]]SEE YOU NEXT TIME.[[black]]\n"))
            break
        elif answer == "1":
            list_currencies(currencies)
        elif answer == "2":
            currency1 = input("Enter your base currency id: \n").upper()
            currency2 = input("What currency id are you converting to? \n").upper()
            amount = input(f"Enter an amount in {currency1}: \n").upper()
            convert_currencies(currency1, currency2, amount)
        elif answer == "3":
            currency1 = input("Enter a base currency id: \n").upper()
            currency2 = input("Enter the next currency id: \n").upper()
            exchange_rate(currency1, currency2)
        elif answer == "4":
            get_countries(currencies)
        else:
            print("You have made an invalid choice.")


def register_to_use():
    """
    Update the register with the new username
    """
    print("\nSignup below: ")
    username = input("Enter your Username: \n")
    print(username)
    worksheet_to_update = SHEET.worksheet("register")

    # Convert the username to a list
    add_to_list = username.split()
    # Update the username to the end of the column
    worksheet_to_update.append_row(add_to_list)
    print(f"You are now a registered user...\n")
    sign_in()


def check_status(name):
    """
    Checks if the user is a registered user
    """
    register = SHEET.worksheet("register")
    data = register.get_all_values()

    register_data = data[1:]
    all_data = []
    for data in register_data:
        for val in data:
            all_data.append(val)
    registered_names = all_data

    if name in registered_names:
        print("Welcome to MyCurrency...\n")
        typewriter(colorRep("[[blue]]The Currency Master.\n[[black]]"))
        print("What will you like to do today?\n")
        start_app()
    else:
        print(
            "You are not a registered user.\n\nYou need to register to use this program."
        )
        register_to_use()


def sign_in():
    """
    Takes in username
    calls to check if username is registered
    """
    username = input(
        "Enter your username: \n"
    )  # Retained as user types it in for proper verification of user
    check_status(username)


def main():
    """
    Starts the application
    """
    print_art()
    sign_in()


if __name__ == "__main__":
    main()
