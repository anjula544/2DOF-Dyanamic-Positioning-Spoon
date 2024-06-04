from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    AccX : int
    AccY : int
    AccZ : int
    GyroX :int
    GyroY :int
    GyroZ: int
    
with open("parkinsom_model.sav", 'rb') as file:
    parkinson_model = pickle.load(file)

@app.post('/parkinson_prediction')  # You missed the leading slash here
def parkinson_pred(input_parameters: model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    accX = input_dictionary['AccX']
    accY = input_dictionary['AccY']
    accZ = input_dictionary['AccZ']
    gyroX = input_dictionary['GyroX']  # Fixed variable name
    gyroY = input_dictionary['GyroY']  # Fixed variable name
    gyroZ = input_dictionary['GyroZ']  # Fixed variable name
    
    input_list = [accX, accY, accZ, gyroX, gyroY, gyroZ]
    
    prediction = parkinson_model.predict([input_list])
    
    if prediction == 'low':
        return "The person has a low level of Parkinson's"
    

    elif prediction == 'mid':
        return "The person has a mid level of Parkinson's"
    else:
        return "The person has a high level of Parkinson's"