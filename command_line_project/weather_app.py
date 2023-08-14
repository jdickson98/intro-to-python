import requests #importing of a library that processes the http requests

def get_weather_data(api_key, location): #defined a function
  url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
  
  response = requests.get(url)   
  response.raise_for_status() 
  return response.json()  #information is stored as JSON in website

def show_my_weather(data): #another function, also asked ChatGPT to help make it colourful
    if data:
        print(f"Weather for \033[1;32m{data['name']}:\033[0m")
        print(f"Temperature: \033[1;31m{data['main']['temp']} °C\033[0m")
        print(f"Condition: \033[1;31m{data['weather'][0]['description']}\033[0m") #index is used to access the first element (dictionary) in the list, which holds details about the current weather conditions.
        print(f"Humidity: \033[1;31m{data['main']['humidity']} %\033[0m")
        print(f"Wind Speed: \033[1;31m{data['wind']['speed']} m/s\033[0m")
    else:
        print("Weather data is not available, unlucky bud")


def main():
  api_key = "90966a4a510aeec452b7b2229314fe67" #got the API key from the openweathermap.com website
  lets_go = True #variable

  #while loop
  while lets_go:
    city = input("Where do you want to know the weather for, even though you're definitely not there?\n")

    data = get_weather_data(api_key, city)
    show_my_weather(data)

    choice = input("Do you wish you were somewhere else? (obviously/i'm good): ")
    if choice.lower() != "obviously":
      lets_go = False

if __name__ == "__main__":
  main()