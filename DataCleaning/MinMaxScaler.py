from sklearn.preprocessing import MinMaxScaler

def Min_Max_Scaler(df,columnName:list[str]):
    print("Min Max Scaler of data")
    Min_Max = MinMaxScaler()
    df[columnName] = Min_Max.fit_transform(df[columnName])
    
    print(df)