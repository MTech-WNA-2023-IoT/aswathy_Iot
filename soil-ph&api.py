import paho.mqtt.client as mqtt
import json
import mysql.connector
import requests

# MQTT broker settings
broker_address = "0.0.0.0"
broker_port = 1883
mqtt_topic = "soilmodeling"

# MySQL database settings
mysql_host = "0.0.0.0"
mysql_user = "pi"
mysql_password = "raspberry"
mysql_database = "myProject"

# Weather API settings
weather_api_key = "YOUR_WEATHER_API_KEY"
weather_api_url = "http://api.weatherapi.com/v1/current.json"
weather_location = "YOUR_LOCATION"

def get_weather_data():
    try:
        params = {
            "key": weather_api_key,
            "q": weather_location,
            "aqi": "no"
        }
        response = requests.get(weather_api_url, params=params)
        data = response.json()
        return {
            "Temperature": data["current"]["temp_c"],
            "Humidity": data["current"]["humidity"]
        }
    except Exception as e:
        print("Error retrieving weather data: ", str(e))
        return None

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    try:
        # Decode the received message payload
        data = msg.payload.decode("utf-8")

        # Parse the JSON data
        json_data = json.loads(data)

        # Get weather data
        weather_data = get_weather_data()

        if weather_data:
            # Include weather data in the JSON
            json_data.update(weather_data)

            # Connect to the MySQL database
            db = mysql.connector.connect(
                host=mysql_host,
                user=mysql_user,
                password=mysql_password,
                database=mysql_database
            )

            # Create a MySQL cursor
            cursor = db.cursor()

            # Insert the received data into the table
            query = "INSERT INTO soilmodeling (`Moisture Value`, `pH Value`) VALUES (%s, %s)"
            values = (
                json_data["Moisture Value"],
                json_data["pH Value"],
               
            )
            cursor.execute(query, values)

            # Commit the changes to the database
            db.commit()

            # Close the database connection
            db.close()

            print("Data saved to MySQL database: ", json_data)
    except Exception as e:
        print("Error: ", str(e))

# Create an MQTT client
client = mqtt.Client()

# Set up the MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT client loop
client.loop_forever()
