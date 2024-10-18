import os
from colorama import Fore
from src.places import Places

pythonversion = "Python 3.10.12"
version = "1.1"
cliMenu = """1 - Configure Search
2 - Paste Results
3 - Exit"""

os.system("clear")
print(Fore.RED + "Enter Google Maps API Key (Must be 39 characters)")
key = input(Fore.WHITE + "> ").strip()
if(len(key) != 39):
    print("API Key must be 39 characters exactly")
    exit()
fulfilled = False

while True:
    os.system("clear")
    print(Fore.RED + "Welcome to SweetMapper " + version)

    print(Fore.WHITE + cliMenu)
    cliInput = input("> ")
    match cliInput:
        case "1":
            os.system("clear")
            print("Enter Place Search (e.g. Restaurant)")
            placeType = input("> ")
            os.system("clear")
            print("Enter Location (e.g. Manchester)")
            location = input("> ")
            os.system("clear")
            print("Enter Radius (e.g. 20)")
            radius = input("> ")
            os.system("clear")
            print("Enter Country (e.g. UK)")
            country = input("> ")
            os.system("clear")
            print("Enter Language (e.g. en-UK)")
            language = input("> ")
            os.system("clear")
            print("Open Now? (e.g. True)")
            open_now = bool(input("> "))
            fulfilled = True
        case "2":
            os.system("clear")
            if(fulfilled):
                print("File Name (e.g \"sweetmap\")")
                filename = input("> ")

                plsr = Places(key, f"{placeType} {location}", location, radius, country, language, open_now=open_now)
                df = plsr.areaSearch()
                plsr.toCSV(plsr.getPlaceIds(df), filename)
            else:
                print(Fore.RED + "Please Fulfill Configure Search First")
                l = input(Fore.WHITE + "Press Enter To Go Back > ")

        case "3":
            break


