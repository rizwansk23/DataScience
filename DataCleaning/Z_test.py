from numpy import sqrt
from scipy import  stats

def z_test():
    
    x=18.1
    u=19
    psd = 2.1
    n = 40
    sl = 0.05
    dof = n-1
    z = (x-u) / (psd/sqrt(n))
    print(z)
    # T Test 
    p = stats.t.cdf(z,dof)
    print(p)
    # Z Test
    p1 = stats.norm.cdf(z)
    print(p1)
    if p>sl:
        print('We accept null hypothesis')
    else:
        print('We reject null hypothesis')
        
def Hypothesis_teting():
    print('------Hypothesis Testing------')
    
    x = Input("Sample Mean (x) = ")
    
    u = Input("Population/Assumed Mean (μ) = ")
    
    sd= Input("Standard Deviation (σ) = ")
    
    n = Input("Sample Size (n) = ")
    
    sl = Input("Alpha Value (α) = ")
    
    if n >= 30:
        print('-----Z-test-----')
        z = (x-u) / (sd/sqrt(n))
        askQuestion = Input("Which Test do you want \n1. Upper Test \n2. Lower Test \n3. Two Tail =")
        match(askQuestion):
            case 1.0 :  
                p = stats.norm.sf(z)
                print(f'{p = }')
            case 2.0 :
                p = stats.norm.cdf(z)
                print(f'{p = }')
            case 3.0 :
                p = stats.norm.sf(z)*2
                print(f'{p = }')
            case _ :
                print("Please enter a valid input")                
        
    else:
        dof = n-1   
        print('-----t-test-----')
        z = (x-u) / (sd/sqrt(n))
        askQuestion = Input("Which Test do you want \n1. Upper Test \n2. Lower Test \n3. Two Tail =")
        match(askQuestion):
            case 1.0 :  
                p = stats.t.sf(z,dof)
                print(f'{p = }')
            case 2.0 :
                p = stats.t.cdf(z,dof)
                print(f'{p = }')
            case 3.0 :
                p = stats.t.sf(z,dof)*2
                print(f'{p = }')
            case _ :
                print("Please enter a valid input")
    

def Input(number:int | float) -> float:
    while True:
        try:
            input_value = float(input(number))
            if input_value < 0.0:
                raise ValueError
            return input_value
        except ValueError :
            print('please enter valid value ')