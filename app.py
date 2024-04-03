from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import requests

app = Flask(__name__)

model=pickle.load(open('models/RandomForest.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("form.html")



# @app.route('/submit', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         try:
#             features = [float(x) for x in request.form.values()]
#             final = [np.array(features)]
#             prediction = model.predict(final)
#             print("Prediction successful:", prediction)
#             return render_template('prediction.html', pred=prediction)
#         except Exception as e:
#             print("An error occurred:", e)
#             return "An error occurred while processing the prediction."
#     else:
#         # Handle GET request (if needed)
#         return render_template("form.html")

feature_names = ['no2','so2','pm2_5','pm10','Leq','DO','pH','BOD','Land_use','NBR']

@app.route('/submit', methods=['GET','POST'])
def submit():
    try:
        features=[float(x) for x in request.form.values()]
        final=[np.array(features)]
        print("Input features:", final)
        prediction = model.predict(final)
        output=int(prediction[0])
        print(output)
        return render_template('prediction.html', result=output)
    except Exception as e:
        print("An error occurred:", e)
        return f"An error occurred while processing the prediction: {str(e)}"

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)