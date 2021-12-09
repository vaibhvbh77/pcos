from flask import Flask, render_template, request
from joblib import load
import numpy as np

model = load('model.joblib')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def basic():

    if request.method == 'POST':
        input_data = [int(x) for x in request.form.values()]
        x_pred = [np.array(input_data)]

        prediction_value = model.predict(x_pred)

        POC_not_detected = 'You are safe. You have no Polycystic ovary syndrome.'
        POC_detected='You have Polycystic ovary syndrome. Please consult with a specialist.' 

        if prediction_value == 0:
            return render_template('index.html', POC_not_detected=POC_not_detected)
        elif prediction_value == 1:
            return render_template('index.html', POC_detected=POC_detected)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
