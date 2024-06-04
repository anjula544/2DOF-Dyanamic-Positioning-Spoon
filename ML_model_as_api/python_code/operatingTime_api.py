from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the trained model from the .sav file
model_file = 'spoon_usage_model_1.sav'
spoon_model = joblib.load(model_file)

class ModelInput(BaseModel):
    AccX: int
    AccY: int
    AccZ: int
    GyroX: int
    GyroY: int
    GyroZ: int

@app.post('/spoon_usage_prediction')
def predict_spoon_usage(input_data: ModelInput):
    # Extract input values from the request
    accX = input_data.AccX
    accY = input_data.AccY
    accZ = input_data.AccZ
    gyroX = input_data.GyroX
    gyroY = input_data.GyroY
    gyroZ = input_data.GyroZ
    
    # Make a prediction using the loaded model
    prediction = spoon_model.predict([[accX, accY, accZ, gyroX, gyroY, gyroZ]])
    
    # Based on the prediction, determine spoon usage time
    if prediction == 1:
        return {"usage_time": "Spoon is in use"}
    else:
        return {"usage_time": "Spoon is not in use"}

# Operating time calculation
operating_time = 0
in_use = False
for prediction in predictions:
    if prediction == 1:  # In use
        if not in_use:  # Start of a new operating interval
            in_use = True
            start_time = data_2.index[predictions == 1][0]  # Assuming the index represents time
    else:  # Not in use
        if in_use:  # End of an operating interval
            in_use = False
            end_time = data_2.index[predictions == 0][0]  # Assuming the index represents time
            operating_time += (end_time - start_time).total_seconds()

# Convert operating time to hours (or any desired unit)
operating_time_hours = operating_time / 3600
print("Operating time:", operating_time_hours, "hours")
