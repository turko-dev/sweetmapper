import googlemaps
import json
import pandas as pd
import os
import time
from .validation import StringValidation, BooleanValidation

class Places:
    def __init__(self, placeType, location, radius, region, language="en-UK", open_now=False):

        #Get Configuration Data
        program_path = os.path.abspath(__file__)
        program_directory = os.path.dirname(program_path)
        with open(f"{program_directory}\\config.json", 'r') as config:
            self.config = json.load(config)

        #placeType validation
        if(StringValidation(placeType)): self.placeType = placeType
        else: raise ValueError("placeType needs to be of type str")

        #location validation
        if(StringValidation(location)): self.location = location
        else: raise ValueError("location needs to be of type str")
        
        #radius validation
        if(StringValidation(radius)): self.radius = radius
        else: raise ValueError("radius needs to be of type str")

        #region validation
        if(StringValidation(region)): self.region = region
        else: raise ValueError("region needs to be of type str")

        #language validation
        if(StringValidation(language)): self.language = language
        else: raise ValueError("language needs to be of type str")
        
        #open_now validation
        if(BooleanValidation(open_now)): self.open_now = open_now
        else: raise ValueError("open_now needs to be of type bool")

        #Main Places DataFrame
        self.dataFrame = None
    """Getters & Setters for all parameters"""
    #PlaceType==============================================
    def getPlaceType(self): return self.placeType
    def setPlaceType(self, newPlaceType):
        if(StringValidation(newPlaceType)): self.placeType = newPlaceType
        else: raise ValueError("newPlaceType needs to be of type str")

    #Location==============================================
    def getLocation(self): return self.location
    def setLocation(self, newLocation):
        if(StringValidation(newLocation)): self.location = newLocation
        else: raise ValueError("newLocation needs to be of type str")

    #Radius==============================================
    def getRadius(self): return self.radius
    def setRadius(self, newRadius):
        if(StringValidation(newRadius)): self.radius = newRadius
        else: raise ValueError("newRadius needs to be of type str")

    #Region==============================================
    def getRegion(self): return self.region
    def setRegion(self, newRegion):
        if(StringValidation(newRegion)): self.region = newRegion
        else: raise ValueError("newRegion needs to be of type str")

    #Language==============================================
    def getLanguage(self): return self.language
    def setLanguage(self, newLanguage):
        if(StringValidation(newLanguage)): self.language = newLanguage
        else: raise ValueError("newLanguage needs to be of type str")

    #OpenNow==============================================
    def getOpenNow(self): return self.open_now
    def setOpenNow(self, newOpenNow):
        if(BooleanValidation(newOpenNow)): self.open_now = newOpenNow
        else: raise ValueError("newOpenNow needs to be of type bool")

    """Configuration Commands"""

    #Version
    def version(self): return f"{self.config["version"]}"

    #__str__ function
    def __str__(self): return f"<{self.config["name"]}/{self.config["version"]}.object.Places>"


    """Functionality"""
    #Search any region of the world and return a table of information
    def areaSearch(self):
        
        """
        Returns a pandas DataFrame with a maximum of 60 results
        """
        print("Give Sweetmapper up to 60 seconds to retrieve data from Google's API")

        #with open("key.txt", "r") as apiKey: key = apiKey.readline()

        client = googlemaps.Client(key="AIzaSyCmWj7tdePc7CKhALMdWEh37A9Xq0nHS9M")

        df = pd.DataFrame({
            "name": [],
            "place_id": [],
            "address": []
        })

        time.sleep(5)

        pageSearch = client.places(self.placeType, 
                                    location=self.location, 
                                    radius=self.radius,
                                    region=self.region,
                                    language=self.language,
                                    open_now=self.open_now,
                                    )
        
        df1 = pd.DataFrame({
            "name": [x["name"] for x in pageSearch["results"]],
            "place_id": [x["place_id"] for x in pageSearch["results"]],
            "address": [x["formatted_address"] for x in pageSearch["results"]]
        })

        df = pd.concat([df, df1], ignore_index=True)

        def passToken(token):

            df = pd.DataFrame({
                            "name": [],
                            "place_id": [],
                            "address": []
                        })
            while True:

                token = token

                if token == "":

                    break

                else:

                    time.sleep(5)

                    searchAgain = client.places(self.placeType, 
                                    location=self.location, 
                                    radius=self.radius,
                                    region=self.region,
                                    language=self.language,
                                    open_now=self.open_now,
                                    page_token=token
                                    )
                    
                    dfName = [x["name"] for x in searchAgain["results"]]

                    dfPlace_id = [x["place_id"] for x in searchAgain["results"]]

                    dfAddress = [x["formatted_address"] for x in searchAgain["results"]]

                    df2 = pd.DataFrame({
                        "name": dfName,
                        "place_id": dfPlace_id,
                        "address": dfAddress
                    })
                    
                    df = pd.concat([df, df2])

                    if "next_page_token" in searchAgain:

                        token = searchAgain["next_page_token"]
                    else:
                        
                        token = ""
            return df
        
        dataFrameLoop = passToken(pageSearch["next_page_token"])

        df = pd.concat([df, dataFrameLoop], ignore_index=True)

        return df

    def getPlaceIds(self, df):

        return [x for x in df.get("place_id")]



    def toCSV(self, listofids, fileName, verbose=False):

        key = None

        #with open("key.txt", "r") as apiKey: key = apiKey.readline()

        client = googlemaps.Client(key="AIzaSyCmWj7tdePc7CKhALMdWEh37A9Xq0nHS9M")    

        nameList = []

        numberList = []

        addressList = []

        websiteList = []

        for x in listofids:

            placeSearch = client.place(x)

            time.sleep(2)
            

            if verbose == True:
                
                if "name" in placeSearch["result"]: print(placeSearch["result"]["name"])
                else: print("No Name Available")

                if "formatted_phone_number" in placeSearch["result"]: print(placeSearch["result"]["formatted_phone_number"])
                else: print("No Number Available")

                if "formatted_address" in placeSearch["result"]: print(placeSearch["result"]["formatted_address"])
                else: print("No Address Available")

                if "website" in placeSearch["result"]: print(placeSearch["result"]["website"])
                else: print("No Website Available")

                print("===================================")
            
            if "name" in placeSearch["result"]:nameList.append(placeSearch["result"]["name"])
            else: nameList.append("N/a")
            

            if "formatted_phone_number" in placeSearch["result"]: numberList.append(placeSearch["result"]["formatted_phone_number"])
            else: numberList.append("N/a")

            if "formatted_address" in placeSearch["result"]: addressList.append(placeSearch["result"]["formatted_address"])
            else: addressList.append("N/a")

            if "website" in placeSearch["result"]: websiteList.append(placeSearch["result"]["website"])
            else: websiteList.append("N/a")

        df = pd.DataFrame({"name":[x for x in nameList],
                           "number":[x for x in numberList],
                           "address":[x for x in addressList],
                           "website":[x for x in websiteList]
                           })
        
        df.to_csv(f"{fileName}.csv", index=False)


    def printPlaces(self, listofids):

        key = None

        #with open("key.txt", "r") as apiKey: key = apiKey.readline()

        client = googlemaps.Client(key="AIzaSyCmWj7tdePc7CKhALMdWEh37A9Xq0nHS9M")     

        for x in listofids:

            placeSearch = client.place(x)

            time.sleep(1.5)

            if "name" in placeSearch["result"]: print(placeSearch["result"]["name"])
            else: print("No Name Available")

            if "formatted_phone_number" in placeSearch["result"]: print(placeSearch["result"]["formatted_phone_number"])
            else: print("No Number Available")

            if "formatted_address" in placeSearch["result"]: print(placeSearch["result"]["formatted_address"])
            else: print("No Address Available")

            if "website" in placeSearch["result"]: print(placeSearch["result"]["website"])
            else: print("No Website Available")

            print("===================================")