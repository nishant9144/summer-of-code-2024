# Import necessary libraries
from fastapi import FastAPI, Request, HTTPException
import xgboost as xgb
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the model
model = xgb.Booster()
model.load_model("your_model_path.model")

# Define the input and output data structures
class InputData(BaseModel):
    # Define the input data structure here
    # For example:
    type: str
    amount: float
    oldbalanceOrg: float
    oldbalanceDest: float
    ...

class OutputData(BaseModel):
    # Define the output data structure here
    # For example:
    isFraud: bool

# Define the prediction endpoint
@app.post("/predict", response_model=OutputData)
async def predict(request: Request):
    # Extract the input data from the request
    input_data = await request.json()

    # Convert the input data to a DataFrame
    df = pd.DataFrame(input_data)

    # Drop unnecessary columns
    df.drop(['nameOrig','nameDest'],axis=1,inplace=True)

    # Create dummy variables for categorical features
    type_dummies = pd.get_dummies(df['type']).astype('int')
    df = pd.concat([df,type_dummies], axis=1)
    df.drop('type', axis=1, inplace=True)

    # Drop oldbalanceOrg and oldbalanceDest columns
    df.drop(columns=['oldbalanceOrg','oldbalanceDest'],inplace=True)

    # Standardize the data
    scaler = StandardScaler()
    x_test = scaler.fit_transform(df)

    # Create a DMatrix for the prediction
    dtest = xgb.DMatrix(x_test, enable_categorical=True)

    # Make the prediction
    prediction = model.predict(dtest)[0]

    # Convert the prediction to a boolean value
    is_fraud = bool(prediction > 0.5)

    # Return the prediction as a JSON response
    return {"isFraud": is_fraud}
