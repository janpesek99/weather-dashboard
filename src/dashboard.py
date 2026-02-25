from rich.console import Console
from rich.panel import Panel
from weather_api import WeatherAPI

# Create a console object for fancy printing
console = Console()

def display_current_weather(weather_data):
    """Display current weather in a nice format"""
    
    # Check if we got valid data
    if not weather_data:
        console.print("[red]❌ City not found! Please check the spelling.[/red]")
        return
    
    # Extract the data we want from the dictionary
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    
    # Format it nicely
    weather_info = f"""
    🌡️  Temperature: {temp}°C (feels like {feels_like}°C)
    ☁️  Conditions: {description.capitalize()}
    💧 Humidity: {humidity}%
    💨 Wind Speed: {wind_speed} m/s
    """
    
    # Create a fancy panel to display it
    panel = Panel(
        weather_info, 
        title=f"🌤️  Weather in {city}, {country}", 
        border_style="blue"
    )
    console.print(panel)

def main():
    # Print a welcome message
    console.print("\n[bold cyan]╔════════════════════════════════╗[/bold cyan]")
    console.print("[bold cyan]║    🌤️  WEATHER DASHBOARD 🌤️    ║[/bold cyan]")
    console.print("[bold cyan]╚════════════════════════════════╝[/bold cyan]\n")
    
    # Create an instance of our WeatherAPI class
    api = WeatherAPI()
    
    # Ask the user for a city name
    city = input("Enter city name: ")
    
    # Get the weather data
    console.print(f"\n[yellow]Fetching weather for {city}...[/yellow]\n")
    current_weather = api.get_current_weather(city)
    
    # Display it
    display_current_weather(current_weather)

# This runs when you execute the file
if __name__ == "__main__":
    main()