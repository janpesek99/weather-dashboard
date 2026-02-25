import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class WeatherAPI:
    def __init__(self):
        # Get the API key from environment variables
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        # Base URL for OpenWeatherMap API
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, city):
        """Get current weather for a city"""
        # Construct the full URL
        url = f"{self.base_url}/weather"
        
        # Parameters to send with the request
        params = {
            'q': city,                    # q = query (city name)
            'appid': self.api_key,        # Your API key
            'units': 'metric'             # Celsius (use 'imperial' for Fahrenheit)
        }
        
        # Make the request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Convert JSON response to Python dictionary
            return response.json()
        else:
            # City not found or other error
            return None
