from sklearn.preprocessing import LabelEncoder
from pandas import get_dummies
from typing import Literal

def Label_Encoder(df , new_column : str , column : str):
    print("Label Encoding")
    label = LabelEncoder()
    df[new_column] = label.fit_transform(df[column])
    
    print(df)
    
def One_hot(df,column:list[str] ,columns_name : list[str],drop_column : bool = False , isDummy : bool = False, DataType : Literal['str','int'] ="int" ):
    print('One hot Encoding')
    
    if drop_column:
        columns_name.remove(columns_name[0])
    
    dummy = get_dummies(df,columns=column, drop_first=drop_column,dummy_na=isDummy,dtype=DataType)
    print(dummy[columns_name])