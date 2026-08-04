from pandas import read_csv
from typing import Literal

def read_file(filePath:str, column_name:list[str] | None  = None,isHeader:bool | None | Literal["infer"] = "infer",useCol : tuple[int] | None = None ,skipRow : int | None = None):
    
    df= read_csv(F"Data/{filePath}",header=isHeader,usecols=useCol,skiprows=skipRow)
    
    if column_name:
        df.columns=column_name
    
    print(df)
    
    return df