from sympy import *
from graeffe_binomial_bound_aga_v2 import graeffe, binomial_bd, graeffe_abs_root_bds
from statistics import mean
import pandas as pd

a1, a2, a3, a4, x, y, z = symbols('a1, a2, a3, a4, x, y, z')

def main():
  # v.1.1 fixed error j+= 1 and average of ratios  
    Polys = []

    """
    f = x**3 - 30*x**2 + 129*x -100
    Polys.append(f)
    f = x**3 + 129*x - 100  # complex roots
    Polys.append(f)
    f = x**3 - 7*x + 7  # real roots
    Polys.append(f)
    f = x**6 + x**5 + 6*x**4 - 5*x**3 +3*x**2 + 2 # Cerlienco
    Polys.append(f)
    f = x**7 - x**3 + 7*x -7
    Polys.append(f)
    f = x**8 +8*x**7 +47*x**6 +136*x**5 +285*x**4 +171*x**3 - 20*x**2 - 21*x+2
    Polys.append(f)
    f = 2*x**8 -16*x**7 +26*x**6 -10*x**5 -41*x**4 +89*x**3 -87*x**2 +52*x-10
    Polys.append(f)
    f = 2*x**8 -22*x**7 +33*x**6 +44*x**5 +10*x**4 -13*x**3 +10*x**2 +45*x-25
    Polys.append(f)
    f = 3*x**8 +23*x**7 +13*x**6 -45*x**5 -253*x**4 +26*x**3 -26*x**2 +16*x+3
    Polys.append(f)
    # Lamagna Computer Algebra Concepts and Techniques chapter 6.8 excerises
    f = x**3 + 14*x**2 + 56*x + 64
    Polys.append(f)
    f = 18*x**3 - 57*x**2 + 53*x -12
    Polys.append(f)
    f = 6*x**3 - 73*x**2 -86*x + 273
    Polys.append(f)
    f = 6*x**4 - x**3 + 4*x**2 -x -2
    Polys.append(f)
    f = 6*x**4 -11*x**3 + 8*x**2 -33*x -30
    Polys.append(f)
    f = 5*x**5 - 6*x**4 -24*x**3 +20*x**2 + 7*x - 2
    Polys.append(f)
    f = 15*x**4 - 11*x**4 + 47*x**3 + 27*x**2 - 38*x + 8
    Polys.append(f)
    # 6.8 - ex.6
    """
    f = 6*x**2 + 11*x - 35
    Polys.append(f)
    f = 25*x**4 -16
    Polys.append(f)
    f = 6*x**4 -19*x**3 +24*x**2 -13*x + 4
    Polys.append(f)
    f = 2*x**6 +2*x**5 +2*x**4 + 4*x**3 + 5*x**2 - 3*x - 2
    Polys.append(f)
    f = 8*x**5 - 48*x**4 + 90*x**3 - 90*x**2 + 117*x -27
    Polys.append(f)
    f = 30*x**5 + 39*x**4 + 35*x**3 + 25*x**2 + 9*x + 2
    Polys.append(f)
    f = 30*x**15 - x
    Polys.append(f)
    
    ################

    factors = [0] * len(Polys)
    bino_bounds = [0] * len(Polys)
    ratio_list = [0] * len(Polys)
    k = 5
    i = 0
    j = 0


    for poly in Polys:    
        factors[j] = (factor(poly))
        f_list = (factor_list(poly))
        if len(f_list[1]) == 1 : # be carefull with the lists appending
            j += 1
            continue # Poly can't be factored
        # finding the maximum coeff of all factors
        max_coeff_list = [0] * len(f_list[1])

        for i in range ( len(f_list[1]) ):
            temp_list = (Poly(f_list[1][i][0],x).coeffs())
            temp_list = map(lambda x : abs(x), temp_list)
            max_coeff_list[i] = max(temp_list)
            
        print("*** Poly factored is :",factor(poly))   
        max_c = max(max_coeff_list)
        print("max of coeff of all factors is:", max_c, '\n')
        bino_bounds[j] = (binomial_bd(poly,x,k))
        print("your binomial_bound is: ",bino_bounds[j],'\n')
        
        # calculating ratio of binomial_bound and max_c
        ratio_list[j] = ((float(bino_bounds[j])) / float(max_c))
        print("your ratio is: ",ratio_list[j], '\n\n\n')
        if ratio_list[j] < 1 :
            print("Warning, ratio should be > 1") # check this case if occured
            raise Exception("This should be checked carefully")
        
        j += 1      
    
    print("Your Average ratio is :", mean(list(filter(lambda num: num != 0, ratio_list))))

    ########## Printing Using Panda Dataframes ############
    
    pd.set_option('display.width', None) # Set it to None to display all columns in the dataframe
    data = { 'Polys': Polys,
             'Binomial_bound': bino_bounds,
             'Ratio': ratio_list }
    df = pd.DataFrame(data)
    print(df)
    df.to_csv("Polys.csv")
    #df[].plot()
    return()
main()