from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder

df=read_csv("Data/Housing.csv")
# print(df)

le=LabelEncoder()
df['mainroad']=le.fit_transform(df['mainroad'])
df['guestroom']=le.fit_transform(df['guestroom'])
df['basement']=le.fit_transform(df['basement'])
df['hotwaterheating']=le.fit_transform(df['hotwaterheating'])
df['airconditioning']=le.fit_transform(df['airconditioning'])
df['prefarea']=le.fit_transform(df['prefarea'])
df['furnishingstatus']=le.fit_transform(df['furnishingstatus'])

x_axis = 'area'
y_axis = 'price'


X, Y = df[[x_axis]].values, df[[y_axis]].values


x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=10)

reg=LinearRegression()
reg.fit(x_train,y_train)
y_predict=reg.predict(x_test)

# Errors

mse=mean_squared_error(y_test,y_predict)
r2=r2_score(y_test,y_predict)
print("Mean Square Error",mse)
print("r2_score",r2)
house_pricing=reg.predict([[5000]])
print(house_pricing)

# Plotting
plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,y_predict,color='blue')
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title(f'{x_axis} vs {y_axis}')
plt.show()