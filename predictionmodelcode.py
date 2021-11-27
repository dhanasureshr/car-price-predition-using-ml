import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import ExtraTreesRegressor


# loading the data set

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
feat_importances = pd.Series(model.feature_importances_,index=X.columns)
feat_importances.nlargest(5).plot(kind='barh')

plt.savefig("ImportantFeatures.png")



