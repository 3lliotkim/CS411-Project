import requests

url = "http://api.weatherapi.com/v1/current.json?key=27c7234523dc4d33bf3185545220612&q=Boston&aqi=no"

hot = False

response = requests.get(url)
json = response.json()
temperature = json["current"]["temp_f"]  #see if it is hot or cold
windSpeed = json["current"]["wind_mph"] #high wind speed = cold
cloud = json["current"]["cloud"]             #cloudy 
precipitation = json["current"]["precip_in"] #rainy
sunny = json["current"]["uv"]                #sunny 


if(sunny >= 6):
    hot == True

print("Temperature:",temperature)
print("Wind Speed:",windSpeed,"mph")
print("Percentage of Cloudiness:",cloud)
print("Rain in inches :",precipitation)
if hot == True:
    print("UV",sunny, "Today is sunny")
else:
    print("UV",sunny, "Today is not very sunny")

