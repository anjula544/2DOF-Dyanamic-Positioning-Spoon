import serial
import requests
import json
import time
import pickle

# Load the trained model from the .sav file
model_file = 'spoon_usage_model_1.sav'
with open(model_file, 'rb') as file:
    spoon_model = pickle.load(file)
# Define the URL where you want to send the prediction
url = 'http://127.0.0.1:8000/spoon_usage_prediction'  # Adjust this to match your desired URL

# Define the serial port
serial_port = 'COM7'  # Adjust this to match your Arduino's serial port
baud_rate = 115200

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
        
        # Make a prediction using the loaded model
        accX = int(data_dict['AccX'])
        accY = int(data_dict['AccY'])
        accZ = int(data_dict['AccZ'])
        gyroX = int(data_dict['GyroX'])
        gyroY = int(data_dict['GyroY'])
        gyroZ = int(data_dict['GyroZ'])
        
        prediction = spoon_model.predict([[accX, accY, accZ, gyroX, gyroY, gyroZ]])
        
        # Send data to the specified URL
        response = requests.post(url, json={'AccX': accX, 'AccY': accY, 'AccZ': accZ, 
                                             'GyroX': gyroX, 'GyroY': gyroY, 'GyroZ': gyroZ})
        
        # Print the response from the server
        print("Response:", response.text)
        
except KeyboardInterrupt:
    print("Stopping...")
    ser.close()
