import requests
import pprint


# API Keys
weather_api_key = "219d6fb739af14e15e0d2859413cea1f"
news_api_key = "78be40e3e1004b60a8c0e17736cb9620"

# URLs
weather_url = "http://api.openweathermap.org/data/2.5/weather?"
news_url = "https://newsapi.org/v2/top-headlines?"
inshort_url = "https://inshorts.deta.dev/news?"

def get_weather(city):
    # Create the URL
    complete_url = weather_url + "appid=" + weather_api_key + "&q=" + city
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

def get_news(city):
    # Create the URL
    complete_url = news_url + "apiKey=" + news_api_key

    # Set Parameters
    url = 'https://newsapi.org/v2/everything?'
    parameters = {
    'q': city, 
    'pageSize': 10, 
    'apiKey': news_api_key
    }

    # Send the request
    response = requests.get(url, params=parameters)

    # Convert the response to JSON format
    news_data = response.json()

    # Return the titles as a list of dictionaries
    return [article["title"] for article in news_data["articles"]]

def getInshortNews(category):
     # Create the URL
    complete_url = inshort_url + "category=" + category

    # Send the request
    response = requests.get(complete_url)

    # Convert the response to JSON format
    news_data = response.json()

    # Return the news data of the first arcticle
    return news_data["data"][0]["content"]

def main(city):
    print(" ")

    # Get the weather data for the specified city
    weather_data = get_weather(city)

    # Get the news data
    news_data = get_news(city)

    # Print the weather data
    pprint.pprint("TEMPERATURE IN " + city.upper())
    pprint.pprint(weather_data)
    print(" ")

    # Print the news data
    pprint.pprint(city.upper() + " NEWS HEADLINES")
    pprint.pprint(news_data)
    print(" ") 

    # Print the news data from Inshort
    pprint.pprint("INTERNATIOMAL NEWS UPDATE")
    pprint.pprint(getInshortNews("all"))
    print(" ")
    
print('Enter a city to retieve weather and news for:')
inputCity = input()
main(str(inputCity))