import urequests as requests 
import ujson as json


url1 = "https://discord.com/api/webhooks/890522840821006366/Ol38KeLTe2aXel4y2ECnDLuiDdilNYiEjrhMYHTKp8FsGyVPn6CFHD5HwM-7nCR8ww0B"
url2 = "https://discord.com/api/webhooks/890543506731446273/ShZkMwZ-fMwA7egdOuGxueSKJyByw204Vt0gYkLkL5xu2TYtEvBiwEMh2ZpKQcNGtAdC"
weather_url = "http://api.openweathermap.org/data/2.5/weather?q=Chennai,IN&APPID=b190a0605344cc4f3af08d0dd473dd25"
headers = {
    'Content-Type': 'application/json'
}


    
weather_data = requests.get(weather_url)
city = input("Enter the city name: ")
country_code = input("Enter the country code: ")
location = 'Location: ' + weather_data.json().get('name') + ' - ' + weather_data.json().get('sys').get('country')
# Weather Description
description = 'Description: ' + weather_data.json().get('weather')[0].get('main')
print(description)

# Temperature
raw_temperature = weather_data.json().get('main').get('temp')-273.15

# Temperature in Celsius
temperature = 'Temperature: ' + str(raw_temperature) + '*C'
#uncomment for temperature in Fahrenheit
#temperature = 'Temperature: ' + str(raw_temperature*(9/5.0)+32) + '*F'
print(temperature)

# Pressure
pressure = 'Pressure: ' + str(weather_data.json().get('main').get('pressure')) + 'hPa'
print(pressure)

# Humidity
humidity = 'Humidity: ' + str(weather_data.json().get('main').get('humidity')) + '%'
print(humidity)

# Wind
wind = 'Wind: ' + str(weather_data.json().get('wind').get('speed')) + 'mps ' + str(weather_data.json().get('wind').get('deg')) + '*'
print(wind)
print(location) 


while True:
     payload = json.dumps({
        "Content": "----Weather Report----\n" + location + "\n" + description + "\n" + temperature + "\n" + pressure + "\n" + humidity + "\n" + wind + "",
        
        })
     response = requests.post(url_2, headers=headers, data=payload)
     print(response.json)
