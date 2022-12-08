import requests
from generate_playlsit import get_playlist
from IPython.display import HTML
url = "WEATHER API URL"

hot = False
playlist_displayed= ""
response = requests.get(url)
json = response.json()
temperature = str(json["current"]["temp_f"])  #see if it is hot or cold
windSpeed = str(json["current"]["wind_mph"]) + " mph" #high wind speed = cold
cloud = str(json["current"]["cloud"]) + " %"            #cloudy 
percipitation = str(json["current"]["precip_in"]) #rainy
sunny = str(json["current"]["uv"])                #sunny 


if(float(sunny) >= 6):
    hot == True
      
if hot == True:
    sunny_txt = "UV" + sunny +  "Today is not very sunny"
else:
    playlist_displayed =get_playlist('spotify', '37i9dQZF1DWSqBruwoIXkA')
   
html_table = playlist_displayed.to_html()

f = open(r"PATH TO weather_page.html ON YOUR PC ", "w+")
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

    <p> How about these songs for today? </p>
    {playlist} 
    <button>
        <a type="button" class="b1" href="https://www.spotify.com">Get My Generated Playlist</a>
    </button>
    
</body>
</html>
'''.format(temp = temperature, wind = windSpeed, cl = cloud, rain = percipitation, playlist = html_table)
f.write(text)
f.close()
print(f)

