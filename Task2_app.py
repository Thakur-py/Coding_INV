import requests

# Function to get weather data
def get_weather_data(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "units": "metric",  # Set this to "imperial" for Fahrenheit
        "appid": api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# Function to display weather information
def display_weather_info(weather_data):
    # Extract relevant data from the API response
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    conditions = weather_data["weather"][0]["description"]

    # Display the weather information
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Conditions: {conditions}")

if __name__ == "__main__":
    api_key = "a227080d21b927acc9d00ddd795d84ca"
    location = input("Enter a city or location: ")

    try:
        weather_data = get_weather_data(api_key, location)
        display_weather_info(weather_data)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
