# Weather App Readme

## Overview

This is a simple weather web application built using Flask, a Python web framework, and integrated with the WeatherAPI to provide weather information based on user input.

## Features

- **Search by Location**: Users can input a specific location and country to get weather information.
- **Popular Cities**: The app also provides information for popular cities as a quick reference.
- **Hourly Forecast**: It displays the hourly weather forecast for the selected location.
- **Responsive Design**: The app is designed to work well on various screen sizes.

## Prerequisites

- Python 3.x
- Flask (Python web framework)
- Requests (HTTP library for Python)

## Installation

1. Clone or download the repository to your local machine.

2. Install the required Python packages using pip:

   ```
   pip install Flask requests
   ```

3. Run the `app.py` file:

   ```
   python app.py
   ```

4. Open a web browser and go to `http://localhost:5000` to access the app.

## Usage

1. Enter a country and location in the respective input fields and click the "Enter" button.

2. The app will display the current weather information for the specified location.

3. Additionally, there is a list of popular cities for quick access. Click on a city name to view its weather information.

## Directory Structure

- `app.py`: Python script containing the Flask application.
- `templates`: Folder containing the HTML templates for the app.
- `static`: Folder containing CSS stylesheets and images used in the app.

## Acknowledgements

- Weather data is obtained from the [WeatherAPI](https://www.weatherapi.com/).

## License

This project is licensed under the [MIT License](LICENSE).

## Authors

Nandakrishnan G D,Navaneeth Krishna and Sarah G Theerthan
