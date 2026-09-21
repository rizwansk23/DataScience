import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler



df = pd.read_csv('Data/wine.csv',header=None,usecols=[0,1,2])
df.columns = ['Class','Alcohol_Level','Malic_Acid']
print(df)

#Min-Max Scalar
mm = MinMaxScaler()
df[['Class','Alcohol_Level','Malic_Acid']]= mm.fit_transform(df[['Class','Alcohol_Level','Malic_Acid']])
print(df)

#Standard Scalar
ss = StandardScaler()
df[['Class','Alcohol_Level','Malic_Acid']] = ss.fit_transform(df[['Class','Alcohol_Level','Malic_Acid']])
print(df)



# ------------------------- iris --------------------------


from sklearn.preprocessing import LabelEncoder 


df_iris = pd.read_csv('Data/iris-id.csv')
print(df_iris)


#label Encoder
le = LabelEncoder()
df_iris['species_ID'] = le.fit_transform(df_iris['species']) # type: ignore
print(df_iris)

#One Hot Encoding
dummy = pd.get_dummies(df_iris,columns=['species'],drop_first=False,dummy_na=False)
print(dummy[['species_setosa','species_versicolor','species_virginica']])

