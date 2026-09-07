from pandas import read_csv
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df=read_csv('Data/salaries.csv')
le=LabelEncoder()
df['company1']=le.fit_transform(df['company'])
df['job1']=le.fit_transform(df['job'])
df['degree1']=le.fit_transform(df['degree'])

dt=DecisionTreeClassifier()
X=df[['company1','job1','degree1']].values

Y=df['salary_more_then_100k'].values

dt.fit(X,Y)
prediction=dt.predict([[0,0,1]])
print(prediction)