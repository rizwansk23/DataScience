import numpy as np
import scipy.stats as stats


def chisquare():
    observed=np.array([[25,30,15],[30,25,40]])
    row_sum=observed.sum(axis = 1)
    col_sum=observed.sum(axis = 0)
    grand_total=observed.sum()
    expected=np.outer(row_sum,col_sum)/grand_total
    print(expected)
    
    dof=(observed.shape[0]-1)*(observed.shape[1]-1)
    chi2=(((observed-expected)**2)/expected).sum()
    p_val=stats.chi2.sf(chi2,df=dof)
    print("Chi-square = ",chi2)
    print("Probability = ",p_val)
    
    # built in function to check chi_sqaure , probability, dof & expected value
    # chi2,p_val,_,_ = stats.chi2_contingency(observed)
    # print(f"{chi2 = }")
    # print(f"{p_val = }")