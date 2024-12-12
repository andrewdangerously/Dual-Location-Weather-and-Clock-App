import tkinter as tk
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk  # Requires Pillow library for image support

# Replace with your actual API key from WeatherAPI
API_KEY = '385fe426e86444fb912175544242511'
ICON_PATH = "./icons/"  # Ensure this path contains your weather icons

# Function to fetch weather data with a timeout
def fetch_weather(location):
    BASE_URL = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        'key': API_KEY,
        'q': location,
        'days': 1,  # Only fetch today's weather
        'aqi': 'no',
        'alerts': 'no'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)  # Added timeout for faster failure
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Function to map weather conditions to icons
def get_weather_icon(condition):
    condition = condition.lower()
    if "rain" in condition:
        return "rain.png"
    elif "cloud" in condition:
        return "cloud.png"
    elif "sun" in condition or "clear" in condition:
        return "sun.png"
    elif "snow" in condition:
        return "snow.png"
    elif "thunder" in condition:
        return "thunder.png"
    else:
        return "default.png"  # Default icon for unknown conditions

# Function to update weather and display data with icons
def update_weather():
    for location, elements in location_frames.items():
        if location == "Guam":
            weather_data = fetch_weather("96910")  # Guam's ZIP code
        else:
            weather_data = fetch_weather(location)

        if "error" not in weather_data:
            condition = weather_data['current']['condition']['text']
            icon_file = ICON_PATH + get_weather_icon(condition)

            try:
                icon_image = Image.open(icon_file).convert("RGBA")  # Ensure transparency is handled correctly
                icon_resized = icon_image.resize((50, 50))  # Resize icon for display
                weather_icon = ImageTk.PhotoImage(icon_resized)
                elements['icon'].config(image=weather_icon)
                elements['icon'].image = weather_icon
            except Exception as e:
                elements['icon'].config(image=None)
                elements['icon'].image = None

            forecast = weather_data['forecast']['forecastday'][0]['day']
            max_temp = forecast['maxtemp_f']
            min_temp = forecast['mintemp_f']
            elements['label'].config(
                text=f"{condition}\nHigh: {max_temp}°F\nLow: {min_temp}°F"
            )
        else:
            elements['label'].config(text="Error fetching data.")
            elements['icon'].config(image=None)

    # Schedule the next weather update after 10 minutes
    root.after(600000, update_weather)

# Function to update digital clocks with date and time
def update_clocks():
    for location, tz in timezones.items():
        current_time = datetime.now(pytz.timezone(tz))
        time_str = current_time.strftime("%I:%M:%S %p")
        date_str = current_time.strftime("%A, %B %d")
        time_labels[location].config(text=time_str)
        date_labels[location].config(text=date_str)

    # Schedule the function to run again after 1000 ms
    root.after(1000, update_clocks)

# Function to hide the mouse cursor after 5 seconds of inactivity
def hide_cursor_after_inactivity():
    root.config(cursor="none")  # Hide the cursor
    # Schedule the next check in 5 seconds
    root.after(5000, hide_cursor_after_inactivity)

# Function to reset the inactivity timer whenever the mouse moves
def reset_cursor_timer(event):
    root.config(cursor="arrow")  # Show the cursor
    root.after(5000, hide_cursor_after_inactivity)  # Restart the timer

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Hearts Across Oceans")
root.config(bg="#FFFFFF")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Assume the taskbar takes up about 40px (you may need to adjust this value based on your setup)
taskbar_height = 40

# Set the window to full-screen but account for the taskbar and stretch horizontally
root.geometry(f"{screen_width}x{screen_height - taskbar_height}+0+0")

# Optional: Make the window borderless
root.attributes("-fullscreen", False)

# Bind mouse movement to reset the cursor timer
root.bind("<Motion>", reset_cursor_timer)

# Start the cursor hiding logic
root.after(5000, hide_cursor_after_inactivity)

# Backgrounds for each location
background_images = {
    "Minnesota": ImageTk.PhotoImage(Image.open(ICON_PATH + "background2.png").resize((screen_width, 200))),
    "Guam": ImageTk.PhotoImage(Image.open(ICON_PATH + "background.png").resize((screen_width, 200))),
}

# Frame configuration for locations
locations = ["Minnesota", "Guam"]
timezones = {"Minnesota": "America/Chicago", "Guam": "Pacific/Guam"}
location_frames = {}
time_labels = {}
date_labels = {}

for location in locations:
    # Create a canvas with the background image
    canvas = tk.Canvas(root, width=screen_width, height=200, bg='black')
    canvas.pack(pady=(0, 20))
    canvas.create_image(0, 0, anchor="nw", image=background_images[location])

    # Create a frame to hold the weather icon and the temperature (on the same line)
    weather_frame = tk.Frame(canvas, bg='black')
    weather_frame_window = canvas.create_window(10, 130, anchor="nw", window=weather_frame)

    # Add the weather icon to the frame
    weather_icon = tk.Label(weather_frame, bg="black")
    weather_icon.pack(side="left", padx=10)

    # Add the weather condition and temperature to the frame
    weather_label = tk.Label(weather_frame, text="", font=("Helvetica", 12), justify="left", fg="white", bg="black")
    weather_label.pack(side="left", padx=10)

    # Create a frame for the time and date (vertical)
    time_frame = tk.Frame(canvas, bg='black')
    time_frame_window = canvas.create_window(10, 10, anchor="nw", window=time_frame)

    # Position the time at the top-left corner
    time_label = tk.Label(time_frame, text="", font=("Courier", 18, "bold"), fg="white", bg="black")
    time_label.pack(anchor="w", padx=10)
    time_labels[location] = time_label

    # Position the date at the top-left corner, below the time
    date_label = tk.Label(time_frame, text="", font=("Helvetica", 14, "italic"), fg="white", bg="black")
    date_label.pack(anchor="w", padx=10)
    date_labels[location] = date_label

    # Location label on the right side, moved up by 10 pixels
    location_label = tk.Label(canvas, text=location, font=("Helvetica", 16, "bold"), fg="white", bg="black")
    canvas.create_window(screen_width - 10, 170, anchor="ne", window=location_label)

    # Store the frame and labels for each location
    location_frames[location] = {"icon": weather_icon, "label": weather_label}

# Initialize weather display and start clocks
update_weather()
update_clocks()

# Run the application
root.mainloop()