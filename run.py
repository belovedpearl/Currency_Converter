import os
from requests import get
from regulator import *
import gspread
from google.oauth2.service_account import Credentials
import json
import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_info(json.loads(os.environ["CREDS"]))
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("currency_converter")


# URL for the get request
BASE_URL = "https://free.currconv.com/"

# Get API key saved in the var environment
KEY = os.environ["API_KEY"]


def get_history():
    """
    Prints the performance data of selected currencies
    """
    clear_screen()
    typewriter(colorRep("[[green]]YOU CAN ONLY GET MAXIMUM 8 DAYS HISTORY OF YOUR SELECTED CURRENCIES[[stop_color]]\n"))
    currency1 = input("What is your base currency?\n").upper()
    currency2 = input("What currency are you checking with?\n").upper()
    number_of_days = int(input("Enter the number of days to view \n"))
    end_date = datetime.datetime.now()
    end_date1 = end_date.date()
   
    start_date = end_date - datetime.timedelta(days=1 * number_of_days)
    start_date1 = start_date.date()
    
    data_link = f"api/v7/convert?q={currency1}_{currency2}&compact-ultra&date={start_date1}&endDate={end_date1}&apiKey={KEY}"
    url = BASE_URL + data_link
    # Access the result key in the json file
    data_returned = get(url).json()
    try:
        stated_values = data_returned["results"][f"{currency1}_{currency2}"]["val"]
        print("Your currency performance is illustrated below: ")
        print(f"Date\t \tValue of {currency1} to {currency2}")
        for key, value in stated_values.items():
            print(str(key) +"\t"+ str(value))
    except:
        print(colorRep("[[red_background]]You have entered an incorrect currency identity, check out the list of countries to get your information[[stop_color]]"))


def get_countries(currencies):
    """
    Gets the list of countries avialable in the url
    """
    # list of countries provided in the API documentation
    countries_link = f"api/v7/countries?apiKey={KEY}"
    url = BASE_URL + countries_link
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

    response = get(url)

    data = response.json()
    # Check for incorrect or unlisted currency
    if data["results"] == {}:
        print(colorRep("[[red_background]]Invalid currencies[[stop_color]]"))
        return
    # Get the rate value into a list
    rate = list(data.values())[1][currency1 + "_" + currency2]["val"]
    print(f"Rate of {currency1} to {currency2}  = {rate}")
    return rate


def convert_currencies():
    """
    Convert one currency to another
    Takes a specified amount in the base currency
    """
    currency1 = input("Enter your base currency id: \n").upper()
    currency2 = input("What currency id are you converting to? \n").upper()
    amount = input(f"Enter an amount in {currency1}: \n").upper()

    rate = exchange_rate(currency1, currency2)
    # Check if returned rate is invalid
    if rate is None:
        return
    # Convert input value to number
    try:
        amount = float(amount)
    # In case of error
    except:
        print(
            colorRep(
                "[[red_background]]You have entered an invalid amount[[stop_color]]"
            )
        )
        return
    converted_amount = rate * amount
    print(f"{amount}{currency1} is equal to {converted_amount:.2f}{currency2}")
    return converted_amount


def list_currencies(currencies):
    """
    List the returned currencies
    """
    typewriter(
        colorRep(
            "[[green]]Getting the list of available currencies...\n[[white]]"
        )
    )
    print()
    typewriter(
        colorRep("Column 1 displays [[red]]IDENTITY[[white]] of currencies.\n")
    )
    typewriter(
        colorRep("Column 2 displays [[red]]NAMES[[white]] of currencies.\n")
    )
    typewriter(
        colorRep(
            "Column 3 displays [[red]]SYMBOLS[[white]] of the currencies.\n"
        )
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
            colorRep(
                f"[[blue]]{identity}[[white]] - {name} - [[red]]{symbol}[[white]]"
            )
        )


def get_currencies():
    """
    Returns the currencies in 
    identity, common name and symbol colums
    """
    # list of currencies provided in the API documentation
    currency_link = f"api/v7/currencies?apiKey={KEY}"
    url = BASE_URL + currency_link
    # Access the result key in the json file
    data = get(url).json()["results"]
    # Convert the returned values to a list
    data = list(data.items())
    data.sort()
    return data


def start_app():
    """
    Welcomes the user
    Prompts user to make a choice
    Continues the program in the path chosen
    """
    currencies = get_currencies()

    print("Welcome to MyCash...\n")
    typewriter(
        colorRep(
            "[[blue_background]]The Currency Master.[[stop_color]][[white]]"
        )
    )
    print("\nWhat will you like to do today?\n")

    typewriter(
        colorRep(
            "Press [[red]]1[[white]] to [[red]]LIST[[white]] the available currencies.\n"
        )
    )
    typewriter(
        colorRep(
            "Press [[red]]2[[white]] to [[red]]CONVERT[[white]] from one currency to another.\n"
        )
    )
    typewriter(
        colorRep(
            "Press [[red]]3[[white]] to get [[red]]EXCHANGE[[white]] rate of two currencies.\n"
        )
    )
    typewriter(
        colorRep(
            "Press [[red]]4[[white]] to [[red]]GET[[white]] a list of available countries.\n"
        )
    )
    typewriter(
        colorRep(
            "Press [[red]]5[[white]] to [[red]]VIEW[[white]] performance data of selected currencies over 8 days.\n\n"
        )
    )

    while True:
        answer = input(
            colorRep("Choose an option or press [[red]]q[[white]] to quit.\n")
        )

        if answer.lower() == "q":
            typewriter("Thank you for using MyCash...\n")
            typewriter(colorRep("[[blue]]SEE YOU NEXT TIME.[[white]]\n"))
            break
        elif answer == "1":
            clear_screen()
            list_currencies(currencies)
        elif answer == "2":
            clear_screen()
            convert_currencies()
        elif answer == "3":
            clear_screen()
            currency1 = input("Enter a base currency id: \n").upper()
            currency2 = input("Enter the next currency id: \n").upper()
            exchange_rate(currency1, currency2)
        elif answer == "4":
            clear_screen()
            get_countries(currencies)
        elif answer == "5":
            get_history()
        else:
            print(colorRep("[[red]]You have made an invalid choice.[[white]]"))


def register_user(name):
    """
    Update the register with the new username
    """
    worksheet_to_update = SHEET.worksheet("register")

    # Convert the username to a list
    add_to_list = name.split()
    # Update the username to the end of the column
    worksheet_to_update.append_row(add_to_list)
    typewriter("...\n")
    typewriter("...\n")
    typewriter(colorRep(f"[[green]]You are now a registered user.\n[[white]]"))


def check_status(name):
    """
    Checks if the user is a registered user
    """
    register = SHEET.worksheet("register")
    data = register.get_all_values()

    register_data = data[1:]
    all_data = []
    for data in register_data:
        for value in data:
            all_data.append(value)
    registered_names = all_data

    if name not in registered_names:
        print("Registering new user...")
        register_user(name)


def sign_in():
    """
    Takes in username
    """
    username = input("Enter your username: \n")
    check_status(username)


def main():
    """
    Starts the application
    """
    print_art()
    sign_in()
    start_app()


if __name__ == "__main__":
    main()

