# importing modules for converting json and requesting:

import requests, json

#connecting with api key openweathermap.org

apiKey="a6416778ab7f76802f5c9af86db4b19b"

# url for website where the json format data shown:

baseURL="https://api.openweathermap.org/data/2.5/weather?q="

# input for the city / state name:
cityname = input("Enter your city : ")

#fatching the json file in python:

completeURL=baseURL + cityname + "&appid=" + apiKey

response = requests.get(completeURL)

#data in json format:

data = response.json()

# testing the json file fatch form browser:
# print(data)

# printing the data which are required json to normal format:

print("Current Temperature ", data["main"]["temp"])
print("Maximum Temperature ", data["main"]["temp_max"])
print("Minimum Temperature ", data["main"]["temp_min"])
print("Humidity ", data["main"]["humidity"])


# Formula for converting in kelvin to celsius :

'''kk=data["main"]["temp"]
C = (kk -273.15)
print(kk)'''
