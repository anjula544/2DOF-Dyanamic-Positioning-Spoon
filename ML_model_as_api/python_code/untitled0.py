import serial
import time
import matplotlib.pyplot as plt

# Define serial port parameters
serial_port = 'COM6'  # Change this to match your serial port
baud_rate = 115200

# Initialize serial connection
ser = serial.Serial(serial_port, baud_rate)
print("Serial connection established.")

# Initialize empty lists to store data
time_values = []
acc_x_values = []
acc_y_values = []
acc_z_values = []
gyro_x_values = []
gyro_y_values = []
gyro_z_values = []

# Define number of data points to plot
num_points = 100

# Read and plot data in real-time
try:
    plt.ion()  # Enable interactive mode
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    while True:
        # Read data from serial port
        line = ser.readline().decode().strip()
        data = line.split(',')
        
        if len(data) == 6:
            time_values.append(time.time())
            acc_x_values.append(float(data[0]))
            acc_y_values.append(float(data[1]))
            acc_z_values.append(float(data[2]))
            gyro_x_values.append(float(data[3]))
            gyro_y_values.append(float(data[4]))
            gyro_z_values.append(float(data[5]))
            
            # Keep only the latest 'num_points' data points
            if len(time_values) > num_points:
                time_values.pop(0)
                acc_x_values.pop(0)
                acc_y_values.pop(0)
                acc_z_values.pop(0)
                gyro_x_values.pop(0)
                gyro_y_values.pop(0)
                gyro_z_values.pop(0)

            # Clear the axes and plot updated data
            axs[0].cla()
            axs[0].plot(time_values, acc_x_values, label='AccX')
            axs[0].plot(time_values, acc_y_values, label='AccY')
            axs[0].plot(time_values, acc_z_values, label='AccZ')
            axs[0].legend()
            axs[0].set_title('Accelerometer Data')
            axs[0].set_xlabel('Time')
            axs[0].set_ylabel('Acceleration')

            axs[1].cla()
            axs[1].plot(time_values, gyro_x_values, label='GyroX')
            axs[1].plot(time_values, gyro_y_values, label='GyroY')
            axs[1].plot(time_values, gyro_z_values, label='GyroZ')
            axs[1].legend()
            axs[1].set_title('Gyroscope Data')
            axs[1].set_xlabel('Time')
            axs[1].set_ylabel('Angular Velocity')

            plt.pause(0.01)

except KeyboardInterrupt:
    print("KeyboardInterrupt: Stopping data acquisition.")

# Close serial connection
ser.close()
print("Serial connection closed.")
