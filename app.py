from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import joblib
import logging
import pandas as pd
import uvicorn

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a FastAPI app instance
app = FastAPI()

# Load the pre-trained machine learning model
model = joblib.load('model.joblib')


# Define the input data model using Pydantic
class InputData(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


# Define the output data model for predictions
class PredictionResult(BaseModel):
    prediction: int


# Function to preprocess input data before making predictions
def preprocess_data(data):
    data_dict = data.dict()

    # Create a DataFrame from the input data
    df = pd.DataFrame(data_dict, index=[0])

    # Drop columns not used in scaling
    data_sc_drop = df.drop(['residual_sugar', 'density'], axis=1)

    # Load the scaler used during model training
    sc1 = joblib.load('sc_model.joblib')

    # Transform the input data using the scaler
    rescaled_data_sc_drop = sc1.transform(data_sc_drop)

    return rescaled_data_sc_drop


# Function to make predictions using the pre-trained model
def predict(model, input_data):
    processed_data = preprocess_data(input_data)

    # Log the input and processed data
    logger.info(f"Input Data: {input_data}")
    logger.info(f"Processed Data: {processed_data}")

    # Make predictions using the model
    prediction = model.predict(processed_data)

    # Log the raw prediction
    logger.info(f"Raw Prediction: {prediction}")

    return prediction.tolist()[0]


# Endpoint to handle prediction requests
@app.post("/predict", response_model=PredictionResult, status_code=status.HTTP_200_OK)
def make_prediction(data: InputData):
    try:
        # Call the predict function and return the result as a JSON response
        prediction = predict(model, data)
        return {"prediction": prediction}
    except Exception as e:
        # Log any errors and return an HTTP 500 Internal Server Error response
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction failed")


# Run the FastAPI app using uvicorn when the script is executed
if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)
