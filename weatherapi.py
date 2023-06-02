import json
import mysql.connector
from urllib.request import urlopen

# Create a user account and obtain an API key from https://www.weatherapi.com
url = "https://api.weatherapi.com/v1/current.json?key=746c5ad6052440c780040657232905&q=kollam&aqi=no"

api_page = urlopen(url)
api = api_page.read()
json_api = json.loads(api)

# print("Raw Data")
# print(json_api)

# Connect to MySQL database
db = mysql.connector.connect(
    host='0.0.0.0',
    user='pi',
    password='raspberry',
    database='weather1'
)
# Execute the create table query
db_cursor = db.cursor()
# db_cursor.execute(create_table_query)

# Extract the relevant data from the JSON response
current_data = json_api['current']
location_data = json_api['location']

# Insert the data into the table
sql = """
INSERT INTO `weather_data` (`location_name`, `region`, `country`, `latitude`, `longitude`, `timezone_id`, `localtime_epoch`, `localtime`, `last_updated_epoch`, `last_updated`, `temp_c`, `temp_f`, `is_day`, `condition_text`, `condition_icon`, `condition_code`, `wind_mph`, `wind_kph`, `wind_degree`, `wind_dir`, `pressure_mb`, `pressure_in`, `precip_mm`, `precip_in`, `humidity`, `cloud`, `feelslike_c`, `feelslike_f`, `vis_km`, `vis_miles`, `uv`, `gust_mph`, `gust_kph`)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
# Prepare the SQL INSERT statement
# sql = "INSERT INTO weather_data (location_name, region, country, latitude, longitude, timezone_id, localtime_epoch, localtime, last_updated_epoch, last_updated, temp_c, temp_f, is_day, condition_text, condition_icon, condition_code, wind_mph, wind_kph, wind_degree, wind_dir, pressure_mb, pressure_in, precip_mm, precip_in, humidity, cloud, feelslike_c, feelslike_f, vis_km, vis_miles, uv, gust_mph, gust_kph) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Prepare the values for the SQL statement
values = (location_data["name"],location_data["region"],location_data["country"],location_data["lat"],location_data["lon"],location_data["tz_id"],location_data["localtime_epoch"],location_data["localtime"],current_data["last_updated_epoch"],current_data["last_updated"],current_data["temp_c"],current_data["temp_f"],current_data["is_day"],current_data["condition"]["text"],current_data["condition"]["icon"],current_data["condition"]["code"],current_data["wind_mph"],current_data["wind_kph"],current_data["wind_degree"],current_data["wind_dir"],current_data["pressure_mb"],current_data["pressure_in"],current_data["precip_mm"],current_data["precip_in"],current_data["humidity"],current_data["cloud"],current_data["feelslike_c"],current_data["feelslike_f"],current_data["vis_km"],current_data["vis_miles"],current_data["uv"],current_data["gust_mph"],current_data["gust_kph"])

# Execute the SQL statement
db_cursor.execute(sql, values)
# Commit the changes

db.commit()

# Close the connection

db.close()

# print("Raw Data")
# print(json_api)

print("Data saved to MySQL successfully!")
