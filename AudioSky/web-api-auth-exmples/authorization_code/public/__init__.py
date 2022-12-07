import requests
url = "WEATHER API URL ACCESS"

hot = False

response = requests.get(url)
json = response.json()
temperature = str(json["current"]["temp_f"])  #see if it is hot or cold
windSpeed = str(json["current"]["wind_mph"]) + " mph" #high wind speed = cold
cloud = str(json["current"]["cloud"]) + " %"            #cloudy 
percipitation = str(json["current"]["precip_in"]) #rainy
sunny = str(json["current"]["uv"])                #sunny 


if(float(sunny) >= 6):
    hot == True

temp_word = "Temperature:"
wind_word = "Wind Speed:"
cloud_word = "Percentage of Cloudiness:"
rain_word = "Rain in inches :"


#temp_txt = temp_word + temperature
#wind_txt = wind_word + windSpeed + "mph"
#cloud_txt = cloud_word + cloud
#rain_txt = rain_word + percipitation


if hot == True:
    sunny_txt = "UV" + sunny + "Today is sunny"
else:
    sunny_txt = "UV" + sunny +  "Today is not very sunny"

#temp_txt = "Todays temperature is {temp} ".format(temp = temperature)
#wind_txt = "Wind Speed {wind} ".format(wind = windSpeed)
#cloud_txt = "Percentage of Cloudiness {cl} ".format(cl = cloud)
#rain_txt = "Rain in Inches {rain} ".format(rain = precipitation)


f = open(r"PATH ON YOUR PC", "w+")
text = '''<!DOCTYPE html>
<html>
<head>
    <link rel = "stylesheet" href= "style_weather.css">
</head>
<body>
    <h1>Today's Weather</h1>
    <p>Today looks like:</p>
    <p>Temperature: {temp} F</p>
    <p>Wind Speed: {wind}</p>
    <p>Percentage of Cloudiness: {cl}</p>
    <p>Rain in Inches: {rain}</p>
    <button>
        <a type="button" class="b1" href="https://www.spotify.com">Get My Generated Playlist</a>
    </button>
    
</body>
</html>
'''.format(temp = temperature, wind = windSpeed, cl = cloud, rain = percipitation)
f.write(text)
f.close()
print(f)

