import math as m 
n=5
r=3
nCr=m.factorial(n)//(m.factorial(r)*m.factorial(n-r))
print(f"Combination(nCr) where n={n} and r={r}: {nCr}")