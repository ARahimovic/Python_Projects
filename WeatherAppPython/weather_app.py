import requests

api_key = "634082ecac66843e0eba6a79d9238cba"

city = input("Enter City : ")

unit_input = int(input("Choose measurement system :\n0 for metric \nany value for imperial\nyour input: "))

unit, unit_symbol = ("metric","°C") if unit_input == 0 else ("imperial","°F") 

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&APPID={api_key}"

req = requests.get(url)
data = req.json()

if(data['cod'] == '404'):
    print("REQUEST ERROR")
else :
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure  = data['main']['pressure']
    weather = data['weather'][0]['description']
    wind = data['wind']['speed']
    print(f"Weather : {weather}")
    print(f"temperature : {temp} {unit_symbol}")
    print(f"humidity : {humidity} %")
    print(f"pressure : {pressure}")
    print(f"wind : {wind} m/s")

    

