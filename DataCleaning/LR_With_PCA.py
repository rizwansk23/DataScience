from pandas import DataFrame,read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = read_csv("Data/iris-id.csv")

X = data.drop(['species'],axis=1)
Y = data['species']

print(X)

s = StandardScaler()
X = s.fit_transform(X)
x_train,x_test,y_train,y_test = train_test_split(X,Y,random_state=40)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(y_pred)

y_predicted = model.predict([[5.4,3,1.7,1.2]])
print(y_predicted)