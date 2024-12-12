# Hearts Across Oceans

## Description
Hearts Across Oceans is a Python application designed to display live weather updates and time for multiple locations in a visually appealing interface. It is great for tracking the time and weather of a friend or loved one. The project is built using the Tkinter library and integrates WeatherAPI to fetch current weather conditions. The interface dynamically updates weather information and clocks, ensuring a real-time experience.

## Features
- Real-time weather updates for multiple locations.
- Digital clocks showing local time and date for each location.
- Dynamic weather icons that visually represent current conditions.
- Background images for locations to enhance user experience.
- Automatic hiding of the mouse cursor after inactivity, with reset on mouse movement.

## Requirements
- Python 3.6+
- Libraries:
  - `tkinter` (standard with Python)
  - `requests`
  - `pytz`
  - `Pillow` (for image support)
- WeatherAPI API key (replace `API_KEY` in the script with your key).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hearts-across-oceans.git
   cd hearts-across-oceans
   ```

2. **Install Required Libraries**:
   ```bash
   pip install requests pytz pillow
   ```

3. **Set Up WeatherAPI Key**:
   - Replace `API_KEY` in the script with your WeatherAPI key.

4. **Ensure Icon Path Exists**:
   - Place your weather icons (e.g., `rain.png`, `sun.png`) in the `./icons/` directory.

## Usage
Run the application using the following command:
```bash
python hearts_across_oceans.py
```

## Customization
- **Add Locations**:
  - Modify the `locations` list and `timezones` dictionary in the script to add or change locations.
- **Background Images**:
  - Update the `background_images` dictionary with new images for each location.
- **Weather Icons**:
  - Add custom weather icons to the `./icons/` directory and update the `get_weather_icon()` function to map conditions to new icons.

## Future Improvements
- Add support for more locations.
- Implement user-configurable settings for locations and update intervals.
- Enhance error handling for API failures or missing icons.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments
- WeatherAPI for providing weather data.
- Pillow library for seamless image processing.

Feel free to contribute to the project by submitting pull requests or issues!

