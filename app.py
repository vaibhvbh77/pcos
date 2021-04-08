from flask import Flask, render_template, request
import pcos_model.py
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def basic():

    if request.method == 'POST':


        Diagnose = request.form['Diagnose']
        Overweight = request.form['Overweight']
        Weightgain = request.form['Weightgain]
        Periods = request.form['Periods']
        Conceiving = request.form['Conceiving']
        AcneOrskinTag= request.form['AcneOrskinTag']
        HairThinning= request.form['HairThinning']
        DarkPatch = request.form['DarkPatch']
        Tiredness = request.form['Tiredness']
        MoodSwings = request.form['MoodSwings']
        CannedFood = request.form['TCannedFood']
        City = request.form['City']

        y_pred = [[Diagnose, Overweight, Weightgain, Periods,Conceiving,AcneOrskinTag,HairThinning,DarkPatch,Tiredness,MoodSwings,CannedFood,TCannedFood]

        trained_model = iris_model.training_model()

        prediction_value = trained_model.predict(y_pred)

        POC_not_detected = 'You have no Polycystic ovary syndrome'
        POC_detected='You have no Polycystic ovary syndrome ,Please consult with an specialist ' 
      


        if prediction_value == 0:
            return render_template('index.html', POC_not_detected=POC_not_detected)
        elif prediction_value == 1:
            return render_template('index.html', POC_detected=POC_detected)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
