import math as m 
n=5
r=3
nPr=m.factorial(n)//m.factorial(n-r)
print(f"Permutation(nPr) where n={n} and r={r}: {nPr}")