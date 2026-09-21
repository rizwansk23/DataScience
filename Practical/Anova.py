import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("College.csv")
Vesasc = np.array(df['Vesasc'])
Nga = np.array(df['Nga'])
Bt = np.array(df['Bt'])

Vesasc_mean = Vesasc.mean()
Nga_mean = Nga.mean()
Bt_mean = Bt.mean()
n = 5
k = 3
N = 15

Total_mean = np.array([Vesasc_mean,Nga_mean,Bt_mean]).mean()
a = (Vesasc_mean-Total_mean)**2
b = (Nga_mean - Total_mean)**2
c = (Bt_mean - Total_mean)**2
total_sum_mean = n*(a+b+c)

ssb = total_sum_mean/(k-1)
ssw = (sum((Vesasc - Vesasc_mean)**2) + sum((Nga - Nga_mean)**2) + sum((Bt - Bt_mean)**2)) / (N-k)

F = ssb/ssw
print("Variance between the group :-" , ssb)
print("Variance within the group :-" , ssw)
print("F statistics score :- ",F)
print("P-value :- ", stats.f.sf(F,(k-1),(N-k)))

F,p_value = stats.f_oneway(Vesasc,Nga,Bt)
print("F Statistics : ",F,"\nP Value : ",p_value)
    