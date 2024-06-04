import tkinter as tk
from collections import Counter

# Initialize predictions list
predictions = []

# Function to update the prediction display
def update_prediction_display():
    if predictions:
        prediction_counter = Counter(predictions)
        most_common_prediction = prediction_counter.most_common(1)[0][0]
        prediction_label.config(text="Most common prediction: " + most_common_prediction)
    else:
        prediction_label.config(text="No predictions yet")

# Create a tkinter window
root = tk.Tk()
root.title("Parkinson's Prediction Display")

# Create a label to display the prediction
prediction_label = tk.Label(root, text="No predictions yet", font=("Arial", 12))
prediction_label.pack(pady=20)

# Function to update predictions list
def add_prediction(prediction):
    predictions.append(prediction)
    update_prediction_display()

# Function to clear predictions list
def clear_predictions():
    predictions.clear()
    update_prediction_display()

# Create a button to clear predictions
clear_button = tk.Button(root, text="Clear Predictions", command=clear_predictions)
clear_button.pack()

# Function to handle window close event
def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI event loop
root.mainloop()
