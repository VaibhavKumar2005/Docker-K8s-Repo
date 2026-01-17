from fastapi import FastAPI
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Initialize the App
app = FastAPI()

# 2. Train the model globally (when the server starts)
print("Training Model...")
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])
model = LinearRegression()
model.fit(X, y)
print("Model Trained and Ready! 🚀")

# 3. Define the "Home" route
@app.get("/")
def home():
    return {"message": "ML API is running! Go to /predict?hours=6 to test."}

# 4. Define the "Prediction" route
@app.get("/predict")
def predict(hours: float):
    # Make the prediction
    prediction = model.predict([[hours]])
    return {
        "input_hours": hours,
        "prediction_score": prediction[0]
    }