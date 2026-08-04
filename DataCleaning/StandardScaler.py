from sklearn.preprocessing import StandardScaler

def Standardition(df,columnName:list[str]):
    print("Standard Scaler of data")
    Standard = StandardScaler()
    df[columnName] = Standard.fit_transform(df[columnName])
    
    print(df)