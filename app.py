from flask import Flask,render_template,request
# used request to catch the values of data in html
# import pcos_model


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def basic():
    if request.method=='POST':

        passenger_class=request.form['pclass']
        age=request.form['age']
        gender=request.form['gender']
        if gender=="male":
            male=1
            female=0
        else:
            female=1
            male=0
        print(passanger_class,age,gender)    
    #     x_pred=[[passenger_class]]    
    #     imported_model=pcos_model.trained_model()
    #     y_pred=imported_model.predict(x_pred)
    #     print(y_pred)
        

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)