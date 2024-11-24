import os
from colorama import Fore
import googlemaps
import pandas as pd
import time

#Add Cities in here
cities = {
    "manchester": [53.4808, -2.2426]
    
}
placeType = "Coffee Shops"
radius = 20
language = "en-UK"
filename = "lol"

def sweetmap(mode, key, placeType, location, radius, language, filename):
    
    if(isinstance(location, dict)):
        pass
    elif(isinstance(location, str)):
        city = location
        location = {"lat": cities[city][0], "lng": cities[city][1]}

    client = googlemaps.Client(key=key)
    time.sleep(3)
    count = 0
    placeIDList = []
    nameList = []
    numberList = []
    addressList = []
    websiteList = []
    pageSearch = client.places(placeType, 
                                    location=location,
                                    language=language,
                                    radius=radius,
                                    open_now=False,
                                    )
    for x in pageSearch["results"]:
        count = count + 1
        placeIDList.append(x["place_id"])
    time.sleep(3)
    skipNext = False
    if(skipNext == False):
        if("next_page_token" in pageSearch):
            pageSearch2 = client.places(placeType, 
                                        location=location,
                                        language=language,
                                        radius=radius,
                                        open_now=False,
                                        page_token=pageSearch["next_page_token"]
                                        )
            for y in pageSearch2["results"]:
                count = count + 1
                placeIDList.append(y["place_id"])
    else:
        skipNext = True
    time.sleep(3)
    if(skipNext == False):
        if("next_page_token" in pageSearch2):
            pageSearch3 = client.places(placeType, 
                                        location=location,
                                        language=language,
                                        radius=radius,
                                        open_now=False,
                                        page_token=pageSearch2["next_page_token"]
                                        )
            for z in pageSearch3["results"]:
                count = count + 1
                placeIDList.append(z["place_id"])
    time.sleep(3)
    

    if(mode == "print" or mode == "both"):

        for a in placeIDList:
            placeIDSearch = client.place(a)
            if "name" in placeIDSearch["result"]: print(placeIDSearch["result"]["name"])
            if "formatted_phone_number" in placeIDSearch["result"]: print(placeIDSearch["result"]["formatted_phone_number"])
            if "formatted_address" in placeIDSearch["result"]: print(placeIDSearch["result"]["formatted_address"])
            if "website" in placeIDSearch["result"]: print(placeIDSearch["result"]["website"])
            print("==============================")

            time.sleep(2)

    if(mode == "csv" or mode == "both"):
        
        for x in placeIDList:
            placeIDSearch = client.place(x)
            if "name" in placeIDSearch["result"]: nameList.append(placeIDSearch["result"]["name"])
            else:nameList.append("N/a")
            if "formatted_phone_number" in placeIDSearch["result"]: numberList.append(placeIDSearch["result"]["formatted_phone_number"])
            else:numberList.append("N/a")
            if "formatted_address" in placeIDSearch["result"]: addressList.append(placeIDSearch["result"]["formatted_address"])
            else:addressList.append("N/a")
            if "website" in placeIDSearch["result"]: websiteList.append(placeIDSearch["result"]["website"])
            else:websiteList.append("N/a")
        df = pd.DataFrame({"name":[x for x in nameList],
                           "number":[x for x in numberList],
                           "address":[x for x in addressList],
                           "website":[x for x in websiteList]
                           })
        df.to_csv(f"{filename}.csv", index=False)



    #if mode == print, print all results
    #if mode == csv, paste all results into CSV file
    #if mode == both, print all results and pastes into csv file
    





pythonversion = "Python 3.10.12"
version = "1.2"
cliMenu = """1 - Configure Search
2 - Paste Results to CSV
3 - Print Results to Screen
4 - Exit"""

import maskpass
os.system("clear")
print(Fore.RED + "Enter Google Maps API Key (Must be 39 characters)")
key = maskpass.askpass(Fore.WHITE + "> ", mask="*").strip()
if(len(key) != 39):
    print("API Key must be 39 characters exactly")
    exit()
fulfilled = False

while True:
    #os.system("clear")
    print(Fore.RED + "Welcome to SweetMapper " + version)

    print(Fore.WHITE + cliMenu)
    cliInput = input("> ")
    os.system("clear")
    
    match cliInput:
        case "1":
            #os.system("clear")
            print("Enter Place Search (e.g. Restaurant)")
            placeType = input("> ")
            #os.system("clear")
            print("Enter City (Press ENTER to enter your own Lat:Lng values)")
            loc = str(input("> ").lower().strip())
            if(loc == ""):
                print("Enter Latitudinal Value (e.g. -33.8599358)")
                lat = float(input("> "))
                #os.system("clear")
                print("Enter Longitudinal Value (e.g. 151.2090295)")
                lng = float(input("> "))
            #os.system("clear")
            print("Enter Radius (e.g. 20)")
            radius = input("> ")
            #os.system("clear")
            print("Enter Country (e.g. UK)")
            country = input("> ")
            #os.system("clear")
            print("Enter Language (e.g. en-UK)")
            language = input("> ")
            fulfilled = True
        case "2":
            os.system("clear")
            if(fulfilled):
                print("File Name (e.g \"sweetmap\")")
                filename = input("> ")
                if(loc != ""):
                    sweetmap("csv", key=key, placeType=placeType, location=loc, radius=radius, language=language, filename=filename)
                else:
                    sweetmap("csv", key=key, placeType=placeType, location={"lat": lat, "lng": lng}, radius=radius, language=language, filename=filename)

            else:
                print(Fore.RED + "Please Fulfill Configure Search First")
                l = input(Fore.WHITE + "Press Enter To Go Back > ")
        case "3":
            if(fulfilled):
                if(loc != ""):
                    sweetmap("print", key=key, placeType=placeType, location=loc, radius=radius, language=language, filename=filename)
                else:
                    sweetmap("print", key=key, placeType=placeType, location={"lat": lat, "lng": lng}, radius=radius, language=language, filename=filename)
                print("===================================")

            else:
                print(Fore.RED + "Please Fulfill Configure Search First")
                l = input(Fore.WHITE + "Press Enter To Go Back > ")
        case "4":
            break


