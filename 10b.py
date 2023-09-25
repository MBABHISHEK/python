import json

def fetch_weather_data(file_path, city_name):

    with open(file_path, 'r') as json_file:
       
        weather_data = json.load(json_file)
      
    city_info = weather_data.get(city_name)
    
    if city_info:
        temperature = city_info.get('Temperature')
        weather = city_info.get('Weather')
    
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}")
        print(f"Weather: {weather}")
    else:
        print(f"Error: City '{city_name}' not found in the weather data.")

weather_file_path = 'weather_data.json'
city_to_fetch = 'Mysore'

fetch_weather_data(weather_file_path, city_to_fetch)
