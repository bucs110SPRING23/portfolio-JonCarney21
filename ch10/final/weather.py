import requests

class WeatherAPIProxy:
    """
    A proxy class for the OpenWeatherMap API.
    """
    def __init__(self, url, key, city):
        self.api_url = url
        self.api_key = key
        self.city = city

    def __str__(self):
        return f"APIProxy with URL: {self.api_url}"

    def handle_weather_request(self):
        # Create the URL
        complete_url = self.api_url + "appid=" + self.api_key + "&q=" + self.city
        #print(complete_url)
        # Send the request
        response = requests.get(complete_url)

        # Convert the response to JSON format
        weather_data = response.json()

        # Check if the request was successful
        if weather_data["cod"] != "404":
            # Get the temperature, humidity and description from the response
            data=weather_data['main']
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]

            # Return the weather data as a dictionary
            return {"temperature": temperature, "humidity": humidity, "description": description}
        else:
            # Return an error message if the request failed
            return {"error": "City not found"}
        