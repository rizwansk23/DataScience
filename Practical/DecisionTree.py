import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("Data/salaries.csv")
print(df)

le = LabelEncoder()
df['company1'] = le.fit_transform(df['company']) # type: ignore
df['job1'] = le.fit_transform(df['job']) #type:ignore
df['degree1'] = le.fit_transform(df['degree']) #type:ignore

dt = DecisionTreeClassifier()
X = df[['company1','job1','degree1']].values

Y = df["salary_more_then_100k"].values

dt.fit(X,Y) # type: ignore

prediction = dt.predict([[0,0,1]])
print("Prediction :",prediction)

# from sklearn.tree import plot_tree
# print("Accuracy:", dt.score(X, Y))
# plt.figure(figsize=(12, 8))
# plot_tree(dt, feature_names=['company','job','degree'], class_names=['<=100k','>100k'], filled=True)
# plt.show()

