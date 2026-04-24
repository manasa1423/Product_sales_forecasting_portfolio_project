from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model when server starts
model = joblib.load("sales_model.pkl")

@app.route("/")
def home():
    return "Sales Forecast API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Example features (change according to your model)
        tv = data["TV"]
        radio = data["Radio"]
        newspaper = data["Newspaper"]

        features = np.array([[tv, radio, newspaper]])
        prediction = model.predict(features)

        return jsonify({
            "Predicted_Sales": float(prediction[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)