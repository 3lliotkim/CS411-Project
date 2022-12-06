import requests
import webbrowser

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

temp_word = "Temperature:"
wind_word = "Wind Speed:"
cloud_word = "Percentage of Cloudiness:"
rain_word = "Rain in inches :"


temp_txt = temp_word + temperature
wind_txt = wind_word + windSpeed + "mph"
cloud_txt = cloud_word + cloud
rain_txt = rain_word + precipitation


if hot == True:
    sunny_txt = "UV" + sunny + "Today is sunny"
else:
    sunny_txt = "UV" + sunny +  "Today is not very sunny"

#temp_txt = "Todays temperature is {temp} ".format(temp = temperature)
#wind_txt = "Wind Speed {wind} ".format(wind = windSpeed)
#cloud_txt = "Percentage of Cloudiness {cl} ".format(cl = cloud)
#rain_txt = "Rain in Inches {rain} ".format(rain = precipitation)


f = open("weather_page.html").read().format(temp = temp_txt, wind = wind_txt, cl = cloud_txt, rain = rain_txt)
#print(f)

'''
message = 
<html>

<head> </head>
<body>
    <h1>  
        temp_txt
    </h1>
    <h2>  
        wind_txt
    </h2>
    <h3>  
        cloud_txt
    </h3>
    <h4>  
        rain_txt
    </h4>
</body>
<html>


f.write(message)
f.close()
'''



