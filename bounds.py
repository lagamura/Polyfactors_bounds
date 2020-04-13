from r_roots_bound import Birkhoff_rootbound, MS_rootbound
from sympy import *
from sympy.abc import x

def binomial_bound(f,delta):
    #assume f is primitive and square free
    p = MS_rootbound(f)
    b_poly = Abs(LC(f)) * (x + p)**delta
    return(b_poly)

def M(f):
    #assuming z_i refers to all roots Comlex and Rationals
    # needs fix complex representation
    roots_list = Poly(f).all_roots()
    product = 0
    for i in range(1,degree(f)+1):
        print(max(1,abs(roots_list[i-1])))
        product *= max(1,abs(roots_list[i-1]))
    return (Abs(LC(f)) * product)

f = 2*x**3 - 7*x**2 + 4*x + 4
f = primitive(f)[1]
print("Step 1: primitive form of f is :",f,'\n')
coeff_factor = primitive(f)[0] #dont forget to multiply at the end
f = sqf_part(f)
print("Step 2: square free part of f is:",f,'\n') # TODO do we need somewhere the other part?

print("Birkhoff ρ_bound is : %.2f" %Birkhoff_rootbound(f))
print("Mignote - Stefanescu ρ_bound is : %.2f" %MS_rootbound(f))

print("Real roots of ",f,"are",real_roots(f),'\n')

for delta in range(1,degree(f)/2 + 1):
    print("Your binomial_poly |LC(f)|(x+ρ)^δ for delta = ",delta, "is", binomial_bound(f,delta))
    
# M Test
f = -3*x**5 + x**2 + 4*x - 2
print(Poly(f).all_roots())
print(M(f)) #need to fix M
