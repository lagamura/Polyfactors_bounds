from sympy import *
from sympy.abc import x
#x, A, y, c, a, z, θ, t, u, v, S1, S3, S9, S27 = symbols('x, A, y, c, a, z, θ, t, u, v, S1, S3, S9, S27')

def Birkhoff_rootbound(f):
    d = degree(f)
    max_l = 0
    for i in range (1,d+1):
        temp = Abs((Poly(f).nth(d-i)/LC(f)))*(binomial(d,i)**-1)**(1/i)
        if temp > max_l : max_l = temp
    B_f = 1 / (2**(1/d) - 1) * max_l
    return(B_f)

#Mignotte and Stefanescu (2002) - firstly by Lagrance on 1769
def MS_rootbound(f):
    Max_list = []
    d = degree(f)
    for i in range (1,d+1):
        Max_list.append(Abs((Poly(f).nth(d-i)/LC(f)))**(1/i))
    Max_list.sort()
    L_f = Max_list[-1] + Max_list[-2]
    return(L_f)

"""
#Usefull random_poly function for statistical analysis
p = random_poly(x,5,-5,5)
print("Your random poly is: ",p,'\n\n')
print("%.2f" %Birkhoff_rootbound(p))
root = real_roots(p)
print(root)
"""

"""
Berlekamp - Zassenhaus algorithm to factorize poly on Z[x]
(1) make f primitive and square-free,
(2) pick a suitable prime p,
(3) determine the factorization in Fp[x],
(4) lift to a factorization modulo a large enough power pk,
(5) recover the true factors in Z[x].
"""
f = 2*x**3 - 7*x**2 + 4*x + 4
f = primitive(f)[1]
print("Step 1: primitive form of f is :",f,'\n')
coeff_factor = primitive(f)[0] #dont forget to multiply at the end
f = sqf_part(f)
print("Step 2: square free part of f is:",f,'\n') # TODO do we need somewhere the other part?

print("Birkhoff ρ_bound is : %.2f" %Birkhoff_rootbound(f))
print("Mignote - Stefanescu ρ_bound is : %.2f" %MS_rootbound(f))

print("Real roots of ",f,"are",real_roots(f),'\n')