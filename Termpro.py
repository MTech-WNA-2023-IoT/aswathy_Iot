import paho.mqtt.client as mqtt
import json
import mysql.connector

# MQTT broker settings
broker_address = "0.0.0.0"
broker_port = 1883
mqtt_topic = "soilph"

# MySQL database settings
mysql_host = "0.0.0.0"
mysql_user = "pi"
mysql_password = "raspberry"
mysql_database = "TProject"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    try:
        # Decode the received message payload
        data = msg.payload.decode("utf-8")
       
        # Parse the JSON data
        json_data = json.loads(data)
       
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
        query = "INSERT INTO soil_ph (Moisture Value,pH Value) VALUES (%s, %s)"
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
