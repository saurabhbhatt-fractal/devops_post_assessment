# Importing required packages
from fastapi import FastAPI
from app.schema import ShipmentFeatures
import joblib
import pandas as pd

# Loading the trained model
try:
    print("loading trained model", end = "..." )
    model = joblib.load("models/model.pkl")
    print("[completed]")
except Exception as e:
    print("[error]")
    print(e)


# Crating an app
app = FastAPI(title="Shipment Delay Predictor")

# Defining Endpoints
@app.post("/predict")
def predict(data: ShipmentFeatures):
    # Converting input to dataframe
    print("="*11)
    print(data)
    print("="*11)
    input_data = pd.DataFrame([data.dict()])

    # Some preprocessing to the input data
    mapping_dicts = {
        "Warehouse_block": {"A":0, "B":1, "C":2, "D":3, "F":4},
        "Mode_of_Shipment": {"Flight":0, "Road":1, "Ship":2},
        "Product_importance": {"low":1, "medium":2, "high":0},
        "Gender": {"M":1, "F":0},
    }

    for col, mapping in mapping_dicts.items():
        input_data[col] = input_data[col].map(mapping)


    # Predictions
    prediction = model.predict(input_data)[0]

    # Returning 
    return {"on_time": bool(prediction)}