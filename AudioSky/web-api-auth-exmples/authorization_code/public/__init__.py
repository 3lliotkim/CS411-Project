import requests
from generate_playlist import get_playlist
from IPython.display import HTML
import random
import pandas as pd
url = "WEATHER API URL"


hot = None
playlist_displayed= ""
response = requests.get(url)
json = response.json()
temperature = str(json["current"]["temp_f"])  #see if it is hot or cold
windSpeed = str(json["current"]["wind_mph"]) + " mph" #high wind speed = cold
cloud = str(json["current"]["cloud"]) + " %"            #cloudy 
percipitation = str(json["current"]["precip_in"]) #rainy
sunny = str(json["current"]["uv"])                #sunny 

rand_int = random.randint(0,10)
if(float(temperature) >= 70):
    hot = True

else:
    hot = False

playlist_displayed = get_playlist('sanjanakasarla', '3CxO6BrNt182XoBqyspADP')
sad_playlist = playlist_displayed[playlist_displayed["Valence"] < .5]
happy_playlist = playlist_displayed[playlist_displayed["Valence"] > .5]

sad_table = sad_playlist.to_html()
happy_table = happy_playlist.to_html()



if hot == True:
    rec_playlist = happy_table
    #playlist_displayed = get_playlist('spotify', '37i9dQZF1EIgEWv28Tpoyq')
if hot == False:
    rec_playlist = sad_table
    #playlist_displayed = get_playlist('spotify', '37i9dQZF1DWSqBruwoIXkA')

html_table = playlist_displayed.to_html()

f = open(r"C:\Users\flore\OneDrive\Desktop\CS411\AudioSky\web-api-auth-examples\authorization_code\public\weather_page.html", "w+")
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
    <p> These songs fit the mood? Too bad if you get sad! </p>
    {playlist}
    <br>
    <br>
    <p> We reccommend these songs </p>

    {rec_playlist}
</body>
</html>
'''.format(temp = temperature, wind = windSpeed, cl = cloud, rain = percipitation, playlist = html_table, rec_playlist = rec_playlist)
f.write(text)
f.close()
print(f)
