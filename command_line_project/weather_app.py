import requests

def get_weather_data(api_key, location): #defined a function
  url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
  
  response = requests.get(url)
  response.raise_for_status() 
  return response.json()

def show_my_weather(data):
  if data: # use of an if/else function
    print("Weather for", data["name"], "(" + data["sys"]["country"] + "):")
    print("Temperature:", data["main"]["temp"], "°C"),
    print("Condition:", data["weather"][0]["description"]) #index is used to access the first element (dictionary) in the list, which holds details about the current weather conditions.
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
  else:
    print("Weather data is not available, unlucky bud")

def main():
  api_key = "90966a4a510aeec452b7b2229314fe67" #got the API key from the openweathermap.com website
  city = input("Where do you want to know the weather for, even though you're definitely not there?\n")

  data = get_weather_data(api_key, city)
  show_my_weather(data)

if __name__ == "__main__":
  main()