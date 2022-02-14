# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Building Flask API

from flask import Flask, request, jsonify
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('rf_model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return "Hello World"


standard_to = StandardScaler()


@app.route('/predict', methods=['POST'])
def predict():
    Fuel_Type_Diesel = 0
    if request.method == 'POST':
        Year = int(request.form.get('Year'))
        Present_Price = float(request.form.get('Present_Price'))
        Kms_Driven = int(request.form.get('Kms_Driven'))
        Owner = int(request.form.get('Owner'))
        Fuel_Type_Petrol = request.form.get('Fuel_Type_Petrol')

        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1

        Year = 2021 - Year

        Seller_Type_Individual = request.form.get('Seller_Type_Individual')

        if Seller_Type_Individual == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        Transmission_Mannual = request.form.get('Transmission_Mannual')

        if Transmission_Mannual == 'Mannual':
            Transmission_Mannual = 1
        else:
            Transmission_Mannual = 0

        # Applying input to the model
        input_query = np.array([[Present_Price, Kms_Driven, Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol,
                                 Seller_Type_Individual, Transmission_Mannual]])
        result = model.predict(input_query)[0]
        output = round(result, 2)
    return jsonify({'Price': str(output)})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
