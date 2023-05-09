import requests

class NewsAPIProxy:

    def __init__(self, url, key, inshort, city):
        self.api_url = url
        self.api_key = key
        self.inshort = inshort
        self.city = city


    def __str__(self):
        return f"APIProxy with URL: {self.api_url}"

    def handle_news_request(self):
        # Create the URL
        complete_url = self.api_url + "apiKey=" + self.api_key

        # Set Parameters
        url = 'https://newsapi.org/v2/everything?'
        parameters = {
        'q': self.city, 
        'pageSize': 10, 
        'apiKey': self.api_key
        }

        # Send the request
        response = requests.get(url, params=parameters)

        # Convert the response to JSON format
        news_data = response.json()

        # Return the titles as a list of dictionaries
        return [article["title"] for article in news_data["articles"]]

    def handle_international_request(self):
        # Create the URL
        complete_url = self.inshort + "category=" + "all"
        # Send the request
        response = requests.get(complete_url)
        # Convert the response to JSON format
        temp_data = response.json()
        # Return the news data of the  first arcticle
        return temp_data["data"][0]["content"]
        
