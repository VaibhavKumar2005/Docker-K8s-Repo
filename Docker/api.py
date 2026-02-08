from fastapi import FastAPI

app = FastAPI()

# No training needed. We simulate the logic.

@app.get("/")
def home():
    return {"message": "Simulated ML API is Online ⚡"}

@app.get("/predict")
def predict(hours: float):
    # Fake Linear Regression Logic: y = 10x
    # (Because your original model trained on 1->10, 2->20, etc.)
    fake_prediction = hours * 10.0
    
    return {
        "input_hours": hours,
        "prediction_score": fake_prediction,
        "model_type": "Simulated (Lightweight)"
    }