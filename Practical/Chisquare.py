import numpy as np
from scipy import stats

###Q1.
print("H0 : mean age >= 19")
print("H1 : mean age < 19")
x = 18.1
u = 19
psd = 2.1
n = 40
sl = 0.05
z = (x-u)/(psd/np.sqrt(n))
p = stats.norm.cdf(z)
print(p)
if p > sl:
    print("Null Hypothesis Wins \n")
else :
    print("Alternate Hypothesis Wins\n")    

###Q2.
print("H0 : Newspaper Price == 100")
print("H1 : Newspaper Price != 100")
x = 95
u = 100
ssd = 20
n = 12
dof = n-1
sl = 0.01
t = (x-u)/(ssd/np.sqrt(n))
t = 2*(stats.t.sf(t,dof))
print(t)
if t > sl:
    print("Null Hypothesis Wins\n")
else :
    print("Alternate Hypothesis Wins\n")

###Q3.
print("H0 : Glucose Level == 100")
print("H1 : Glucose Level != 100")
x = 140
u = 100
psd = 15
n = 30
sl = 0.05
z = (x-u)/(psd/np.sqrt(n))
p = 2*(stats.norm.sf(z))
print(p)
if p > sl:
    print("Null Hypothesis Wins\n")
else :
    print("Alternate Hypothesis Wins\n")
###Q4.
print("H0 : Screen Time <= 4.5")
print("H1 : Screen Time > 4.5")
x = 4.75
u = 4.5
psd = 2.0
n = 15
dof = n-1
sl = 0.05
z = (x-u)/(psd/np.sqrt(n))
p = stats.t.sf(z,dof)
print(p)
if p > sl:
    print("Null Hypothesis Wins\n")
else :
    print("Alternate Hypothesis Wins\n")

###Q5.
print("H0 : Sleep Time < 7")
print("H1 : Sleep Time >= 7")
x = 7.24
u = 7
psd = 1.93
n = 22
dof = n-1
sl = 0.05
z = (x-u)/(psd/np.sqrt(n))
p = stats.t.sf(z,dof)
print(p)
if p > sl:
    print("Null Hypothesis Wins\n")
else :
    print("Alternate Hypothesis Wins\n")

###Q6.
print("H0 : Tire Average => 50000")
print("H1 : Sleep Time < 50000")
x = 46500
u = 50000
psd = 8000
n = 28
dof = n-1
sl = 0.05
z = (x-u)/(psd/np.sqrt(n))
p = stats.norm.cdf(z)
print(p)
if p > sl:
    print("Null Hypothesis Wins\n")
else :
    print("Alternate Hypothesis Wins\n")



