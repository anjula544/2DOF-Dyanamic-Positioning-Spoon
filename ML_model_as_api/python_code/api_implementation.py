import serial
import requests
import json
import time

# Define the serial port
serial_port = 'COM6'  # Adjust this to match your Arduino's serial port
baud_rate = 115200

# Define the URL where you want to send the prediction
url = 'http://127.0.0.1:8000/parkinson_prediction'  # Adjust this to match your desired URL

# Open serial connection
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        # Read line from serial
        line = ser.readline().decode('latin-1').strip()

        # Split the line into key-value pairs
        items = line.split(",")
        data_dict = {}
        for item in items:
            pair = item.split(":")
            if len(pair) == 2:
                key, value = pair
                data_dict[key.strip()] = value.strip()
        
        # Send data to the specified URL
        response = requests.post(url, json=data_dict)
        
        # Print the response from the server
        print("Response:", response.text)
        
except KeyboardInterrupt:
    print("Stopping...")
    ser.close()

