# Python requests module to call the API using requests.get().
import requests
# Python json module to parse the response coming from the API.
import json
# Python pandas library to convert the JSON into CSV format.
import pandas as pd

# Defining the initial offset as 0 as we need to call the endpoint mulitple times in real time as there are millions of records. 
# But in this particular case we are calling the endpoint 5 times to make sure we are considering calling API multiple times.
# If we don't consider to call the API multiple times, then the given API/endpoint will only give first 1000 records.
offset = 0
final_write_object = []
while offset <= 4000 :
  URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=1000&$offset="+str(offset) 
  response = requests.get(url = URL)
  json_data = json.loads(response.text)
  final_write_object += json_data
  offset += 1000

write_object = json.dumps(final_write_object, indent = 2)

# Writing the JSON response accumulated from multiple attempts into the JSON file in the on-premise.
with open("/Users/Manipal/Python/NYC311Data.json", "w") as outfile: 
    outfile.write(write_object)

# Writing the data in JSON file in to the CSV file.
df = pd.read_json (r'/Users/Manipal/Python/NYC311Data.json')
df.to_csv ('/Users/Manipal/Python/NYC311Data.csv', index = None)