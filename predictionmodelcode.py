import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV

import pickle

import os

# loading the data set
from sklearn.model_selection import train_test_split

df = pd.read_csv('Car data.csv')

# removing car name
final_dataset = df[['Year','Selling_Price','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner']]

# adding current year columns
final_dataset['Current Year']=2021
# Calculate the number of years (no_Years), how many years ago owner bought a car
final_dataset['No_Year'] = final_dataset['Current Year'] - final_dataset['Year']

# droping the temperory features
final_dataset.drop(['Year'],axis=1,inplace=True)
final_dataset = final_dataset.drop(['Current Year'],axis=1)

# Checking the correleation between features
# corrmat = df.corr()
# top_corr_features = corrmat.index
# plt.figure(figsize=(10,10))
# # plot head map
# g = sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")
# plt.savefig("Feature_correlation.png")

# Encoding categorical data
final_dataset =  pd.get_dummies(final_dataset,drop_first=True)

# separate the dependent & independent feature
X=final_dataset.iloc[:,1:]
y=final_dataset.iloc[:,0]

# Checking the important features
model = ExtraTreesRegressor()
model.fit(X,y)

# plot graph of geature importances for better visualization
# feat_importances = pd.Series(model.feature_importances_,index=X.columns)
# feat_importances.nlargest(5).plot(kind='barh')
#
# plt.savefig("ImportantFeatures.png")

# Split the data into train & test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
regressor = RandomForestRegressor()

n_estimators = [int(x) for x in np.linspace(start =100, stop =1200, num=12)]

# Number of features to consider at every split
max_features = ['auto', 'sqet']

# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5,30,num=6)]

# minimum number of samples required to split a node
min_samples_split = [2, 5, 10, 15, 100]

# Minimum number of samples required at each leaf node

min_samples_leaf = [1, 2, 5, 10]

random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split':min_samples_split,
               'min_samples_leaf': min_samples_leaf}


random_var = RandomizedSearchCV(estimator=regressor, param_distributions= random_grid, scoring='neg_mean_squared_error', n_iter = 10, cv = 5, verbose=2, random_state=42,n_jobs=1)

random_var.fit(X_train,y_train)

pickle_file = open('rf_model.pkl','wb');
pickle.dump(random_var,pickle_file)
# Displaying the final dataset with full features
# pd.set_option('max_columns', None)
# print(final_dataset)
# print(final_dataset.columns.tolist())




# Loading the model from pickle test
filename = 'rf_model.pkl'
score={}
if os.path.getsize(filename) > 0:
    with open(filename, "rb") as f:
        unpickler = pickle.Unpickler(f)
        score =  unpickler.load()
prediction = score.predict([[5, 2700, 0, 7, 0, 1, 0, 1]])
rr=round(prediction[0], 2)
print(rr)







