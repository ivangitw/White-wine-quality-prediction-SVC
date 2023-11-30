import requests

def predict_and_print(features):
    resp = requests.post("http://127.0.0.1:8000/predict", json=features)
    print(f"Input features: {features}")
    print(f"Predicted: {resp.json()}")
    print("----")

# Example of multiple data sets
features_list = [
    {
        "fixed_acidity": 7.2,
        "volatile_acidity": 0.23,
        "citric_acid": 0.32,
        "residual_sugar": 8.5,
        "chlorides": 0.058,
        "free_sulfur_dioxide": 47.0,
        "total_sulfur_dioxide": 186.0,
        "density": 0.99560,
        "pH": 3.19,
        "sulphates": 0.40,
        "alcohol": 9.9
    },
    {
    "fixed_acidity": 6.2,
    "volatile_acidity": 0.66,
    "citric_acid": 0.48,
    "residual_sugar": 1.2,
    "chlorides": 0.029,
    "free_sulfur_dioxide": 29.0,
    "total_sulfur_dioxide": 75.0,
    "density": 0.98920,
    "pH": 3.33,
    "sulphates": 0.39,
    "alcohol": 12.80
    },
    {
    "fixed_acidity": 6.4,
    "volatile_acidity": 0.23,
    "citric_acid": 0.35,
    "residual_sugar": 10.3,
    "chlorides": 0.042,
    "free_sulfur_dioxide": 54.0,
    "total_sulfur_dioxide": 140.0,
    "density": 0.99670,
    "pH": 3.23,
    "sulphates": 0.47,
    "alcohol": 9.2
    },
{
    "fixed_acidity": 8.5,
    "volatile_acidity": 0.26,
    "citric_acid": 0.21,
    "residual_sugar": 16.2,
    "chlorides": 0.074,
    "free_sulfur_dioxide": 41.0,
    "total_sulfur_dioxide": 197.0,
    "density": 0.99800,
    "pH": 3.02,
    "sulphates": 0.50,
    "alcohol": 9.8
},
{
    "fixed_acidity": 6.6,
    "volatile_acidity": 0.36,
    "citric_acid": 0.29,
    "residual_sugar": 1.6,
    "chlorides": 0.021,
    "free_sulfur_dioxide": 24.0,
    "total_sulfur_dioxide": 85.0,
    "density": 0.98965,
    "pH": 3.41,
    "sulphates": 0.61,
    "alcohol": 12.4
}
]

# Send a query and output results for each data set
[predict_and_print(features) for features in features_list]
