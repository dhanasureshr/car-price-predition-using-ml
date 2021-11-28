# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Building Flask API

from flask import Flask,request,jsonify
import numpy as np
import  pickle


model = pickle.load(open('rf_model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form.get('Year'))
        Present_Price=float(request.form.get('Present_Price'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
