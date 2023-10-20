from flask import Flask, request, render_template
import requests
from datetime import datetime

now = datetime.now().hour
app = Flask(__name__)

def get_location_suggestions(query):
    suggested_locations = [
        'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai',
        'Kolkata', 'Pune', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur',
        'Visakhapatnam', 'Indore', 'Thane', 'Bhopal', 'Patna', 'Vadodara',
        'Ghaziabad', 'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut',
        'Rajkot', 'Varanasi', 'Srinagar', 'Aurangabad', 'Dhanbad', 'Amritsar',
        'Navi Mumbai', 'Allahabad', 'Howrah', 'Gwalior', 'Jabalpur', 'Coimbatore',
        'Vijayawada', 'Jodhpur', 'Madurai', 'Raipur', 'Kota', 'Guwahati',
        'Chandigarh', 'Solapur', 'Hubli', 'Dharwad', 'Bareilly', 'Moradabad',
        'Mysore', 'Gurgaon', 'Aligarh', 'Jalandhar', 'Tiruchirapalli', 'Bhubaneswar',
        'Salem', 'Mira-Bhayandar', 'Warangal', 'Thiruvananthapuram', 'Bhiwandi',
        'Saharanpur', 'Gorakhpur', 'Guntur', 'Bikaner', 'Amravati', 'Noida',
        'Jamshedpur', 'Bhilai', 'Cuttack', 'Firozabad', 'Kochi', 'Nellore',
        'Bhavnagar', 'Dehradun', 'Durgapur', 'Asansol', 'Rourkela', 'Nanded',
        'Kolhapur', 'Ajmer', 'Akola', 'Gulbarga', 'Jamnagar', 'Ujjain',
        'Loni', 'Siliguri', 'Jhansi', 'Ulhasnagar', 'Jammu', 'Sangli-Miraj & Kupwad',
        'Mangalore', 'Erode', 'Belgaum', 'Ambattur', 'Tirunelveli', 'Malegaon',
        'Gaya', 'Jalgaon', 'Udaipur', 'Maheshtala', 'Tirupur', 'Davanagere'
    ]

    return [location for location in suggested_locations if query.lower() in location.lower()]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    loc = request.form['location']
    country = request.form['country']

    url = f"http://api.weatherapi.com/v1/current.json?key=87a44b75adab42b597544223231910&q={loc},{country}&aqi=no"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        name = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        localtime = data['location']['localtime']
        condition_text = data['current']['condition']['text']
        condition_icon = data['current']['condition']['icon']
        humidity = data['current']['humidity']
        cloud = data['current']['cloud']
        visibility = data['current']['vis_km']
        temp_c = data['current']['temp_c']
        temp_f = data['current']['temp_f']
        feelslike_c = data['current']['feelslike_c']
        feelslike_f = data['current']['feelslike_f']
        forecast_url = f"http://api.weatherapi.com/v1/forecast.json?key=87a44b75adab42b597544223231910&q={loc},{country}&days=1&hour={now}&aqi=no&alerts=no"
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            hourly_forecast = forecast_data['forecast']['forecastday'][0]['hour']
        else:
            hourly_forecast = []


        return render_template('weather.html', 
                               name=name, region=region, country=country, localtime=localtime,
                               condition_icon=condition_icon, condition_text=condition_text,
                               humidity=humidity, cloud=cloud, visibility=visibility,
                               temp_c=temp_c, temp_f=temp_f, feelslike_c=feelslike_c, feelslike_f=feelslike_f,
                               hourly_forecast=hourly_forecast)
    else:
        return render_template('location_not_found.html', location=loc)
if __name__=="__main__":
    app.run(debug=True)