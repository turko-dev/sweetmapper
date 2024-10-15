from src.places import Places

key = ""
#This will initialise the search type
test = Places(key, "restaurant manchester", "manchester", "20", "UK", "en-UK", open_now=False)

#This return 60 google maps results into a DataFrame
df = test.areaSearch()

#This will print the phone numbers of all the places
#test.toCSV(test.getPlaceIds(df))

test.toCSV(test.getPlaceIds(df), "test")