import numpy as np
from scipy import stats

observed = np.array([12,10,8,10,11,9])
print("Observed frequency : ",observed)
faces = 6
expected = np.array([observed.sum()/faces]*faces)
print("Expected frequency : ",expected)
dof = faces-1

chi2 = sum(((observed-expected)**2)/expected)
print("Chisquare Value : ",chi2)
p_value = stats.chi2.sf(chi2,dof)
print("Probability : ",p_value)

chi2,p_value = stats.chisquare(observed,expected)
print("Built-In Formula ",p_value)




#  ------------------------- case 2 ------------------------

observed = np.array([[25,30,15],[30,25,40]])
print("Array : \n",observed)
row_sum = observed.sum(axis=1)
col_sum = observed.sum(axis=0)
grand_total = observed.sum()
expected = np.outer(row_sum,col_sum)/grand_total
print(expected)
dof = (observed.shape[0]-1)*(observed.shape[1]-1)

chi2 = (((observed-expected)**2)/expected).sum()
print("Chisquare Value : ",chi2)
p_value = stats.chi2.sf(chi2,dof)
print("Probability : ",p_value)

chi2,p_value,dof,expected = stats.chi2_contingency(observed)
print("Built-In Formula ",p_value)
