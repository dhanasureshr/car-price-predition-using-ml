# Builting a Machine Learning model

import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import pickle

# loading the data set
from sklearn.model_selection import train_test_split
df = pd.read_csv('Car data.csv')
# removing car name
final_dataset = df[['Year', 'Selling_Price', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
# adding current year columns
final_dataset['Current Year'] = 2021
# Calculate the number of years (no_Years), how many years ago owner bought a car
final_dataset['No_Year'] = final_dataset['Current Year'] - final_dataset['Year']
# droping the temperory features
final_dataset.drop(['Year'], axis=1, inplace=True)
final_dataset = final_dataset.drop(['Current Year'], axis=1)
# Encoding categorical data
final_dataset = pd.get_dummies(final_dataset, drop_first=True)
# separate the dependent & independent feature
X = final_dataset.iloc[:, 1:]
y = final_dataset.iloc[:, 0]
# Checking the important features
model = ExtraTreesRegressor()
model.fit(X, y)
# Split the data into train & test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
re = RandomForestRegressor()
n_estimators = [int(x) for x in np.linspace(start=100, stop=1200, num=12)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 30, num=6)]
# minimum number of samples required to split a node
min_samples_split = [2, 5, 10, 15, 100]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 5, 10]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}

random_var = RandomizedSearchCV(estimator=re, param_distributions=random_grid, scoring='neg_mean_squared_error',
                                n_iter=10, cv=5, verbose=2, random_state=42, n_jobs=1)

random_var.fit(X_train, y_train)

f = 'model.pkl'
with open(f, 'wb') as file:
    pickle.dump(random_var, file)

