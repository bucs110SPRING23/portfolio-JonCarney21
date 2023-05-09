import pprint
from weather import WeatherAPIProxy
from city_news import NewsAPIProxy

# Constants

## API Keys
weather_api_key = "219d6fb739af14e15e0d2859413cea1f"
news_api_key = "78be40e3e1004b60a8c0e17736cb9620"

## URLs
weather_url = "http://api.openweathermap.org/data/2.5/weather?"
news_url = "https://newsapi.org/v2/top-headlines?"
inshort_url = "https://inshorts.deta.dev/news?"

def main(inputcity):
    print(" ")
    news_data = NewsAPIProxy(news_url, news_api_key, inshort_url, inputcity)

    weather_data = WeatherAPIProxy(weather_url, weather_api_key, inputcity)

    international_data = NewsAPIProxy(news_url, news_api_key, inshort_url, inputcity)
    # Print the weather data
    pprint.pprint("TEMPERATURE IN " + inputcity.upper())
    pprint.pprint(weather_data.handle_weather_request())
    print(" ")

    # Print the news data
    pprint.pprint(inputcity.upper() + " NEWS HEADLINES")
    pprint.pprint(news_data.handle_news_request())
    print(" ") 

    # Print the news data from Inshort
    pprint.pprint("INTERNATIOMAL NEWS UPDATE")
    pprint.pprint(international_data.handle_international_request())
    print(" ")

inputcity = input('Enter a city to retieve weather and news for:\n')
main(inputcity)

