from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("laptop_prices_model_82.pkl")
encoder = joblib.load("encoder.pkl")


@app.route('/api/predict', methods=['POST'])
def api_predict():

    data = request.get_json()

    user_data = pd.DataFrame([data])

    encoded_data = encoder.transform(user_data)

    prediction = model.predict(encoded_data)

    return jsonify({
        "predicted_price": float(prediction[0])
    })


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    user_data = pd.DataFrame([{
        "Company": request.form["Company"],
        "TypeName": request.form["TypeName"],
        "Inches": float(request.form["Inches"]),
        "ScreenResolution": request.form["ScreenResolution"],
        "Ram": request.form["Ram"],
        "Cpu Brand": request.form["Cpu Brand"],
        "Cpu Model": request.form["Cpu Model"],
        "SSD": int(request.form["SSD"]),
        "HDD": int(request.form["HDD"]),
        "Gpu Brand": request.form["Gpu Brand"],
        "Gpu Model": request.form["Gpu Model"]
    }])

    encoded_data = encoder.transform(user_data)

    prediction = model.predict(encoded_data)

    predicted_price = round(prediction[0], 2)

    return render_template(
        'index.html',
        prediction_text=f"Estimated Laptop Price: ${predicted_price}"
    )


if __name__ == '__main__':
    app.run(debug=True)
    
    