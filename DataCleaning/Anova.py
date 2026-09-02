import pandas as pd
import numpy as np
from scipy import stats

def anova():
    df=pd.read_csv("College.csv")
    
    ves=np.array(f"df{'VESASC'}")
    nga=np.array(f"df{'NGA'}")
    bt=np.array(f"df({'BT'})")