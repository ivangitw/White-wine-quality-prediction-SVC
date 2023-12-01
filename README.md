## Description
This project implements a support vector machine (SVC) model for predicting the quality of white wine. The prediction model is exposed through a FastAPI web service and deployed using Docker for easy scalability and deployment.

## Requirements
- Docker

## How to Run
1. Install and run Docker.
2. Build Docker image using `docker build -t wine-quality-predictor .`.
3. Run Docker container using `docker run -d -p 8000:80 wine-quality-predictor`.
4. Go to `http://127.0.0.1:8000/docs` to see all available methods of the API.

## Project Structure
- [app.py](app.py): Contains the logic for the FastAPI API.
- [query_example.py](query_example.py): A script to check if the Docker container is working properly.
- [Dockerfile](Dockerfile): Describes the Docker image used to run the API.
- [requirements.txt](requirements.txt): Lists project dependencies.

## Model Files
- [model.joblib](model.joblib): The trained Support Vector Machine (SVC) model for white wine quality prediction.
- [sc_model.joblib](sc_model.joblib): The StandardScaler model used for data preprocessing.

## Additional Notes
- Make sure port 8000 is available before running the Docker container.
- API documentation is available at `http://127.0.0.1:8000/docs`.

Input variables:

    1 - fixed acidity (float)
   
    2 - volatile acidity (float)
   
    3 - citric acid (float)
   
    4 - residual sugar (float)
   
    5 - chlorides (float)
   
    6 - free sulfur dioxide (float)
   
    7 - total sulfur dioxide (float)
   
    8 - density (float)
   
    9 - pH (float)
   
    10 - sulphates (float)
   
    11 - alcohol (float)
   
Output variable: 

    12 - quality (score between 0 and 10) (int)

