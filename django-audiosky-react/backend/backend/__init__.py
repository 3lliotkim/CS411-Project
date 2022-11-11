import requests

url = "http://api.weatherapi.com/v1/current.json?key=620989d8befc4782ac2172558221111&q=Boston&aqi=no"

response = requests.get(url)
json = response.json()
temperature = json["current"]["temp_f"]
feelslike = json["current"]["feelslike_f"]
windSpeed = json["current"]["wind_mph"]
print("Todays Temperature:",temperature)
print("Todays feels like:",feelslike)
print("Todays Wind Speed:",windSpeed,"mph")
