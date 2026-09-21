import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Data/Housing.csv")
# print(df.head)

le = LabelEncoder()
df['mainroad'] = le.fit_transform(df['mainroad']) # type: ignore
df['guestroom'] = le.fit_transform(df['guestroom']) # type: ignore
df['basement'] = le.fit_transform(df['basement']) # type: ignore
df['hotwaterheating'] = le.fit_transform(df['hotwaterheating']) # type: ignore
df['airconditioning'] = le.fit_transform(df['airconditioning']) # type: ignore
df['prefarea'] = le.fit_transform(df['prefarea']) # type: ignore
df['furnishingstatus'] = le.fit_transform(df['furnishingstatus']) # type: ignore

#Single Linear Regression
X = df[['area']].values

#Multiple Linear Regression
X = df.drop('price',axis=1).values 

Y = df[['price']].values
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
reg = LinearRegression()
reg.fit(x_train,y_train)
y_prediction = reg.predict(x_test)

mse = mean_squared_error(y_test,y_prediction)
r2 = r2_score(y_test,y_prediction)

print("Mean Squared Error : ",mse)
print("R Squared",r2)

#Single Linear Regression
house_price = reg.predict([[5000]]) # type: ignore
print(house_price)

# #Multiple Linear Regression
house_price = reg.predict([[7420,4,2,3,1,0,0,0,1,2,1,0]]) # type: ignore
print(house_price)

# Plotting For Single Regression (needs X = df[['area']].values)
plt.scatter(x_test,y_test,color = 'blue')
plt.plot(x_test,y_prediction,color = 'red')
plt.xlabel('area')
plt.ylabel('price')
plt.title("Area vs House Prices")
plt.show()

# Plotting For Multiple Regression (actual vs predicted)
plt.scatter(y_test,y_prediction,color = 'blue')
plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],color = 'red')
plt.xlabel('Actual price')
plt.ylabel('Predicted price')
plt.title("Actual vs Predicted House Prices")
plt.show()
