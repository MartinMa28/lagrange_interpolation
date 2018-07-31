import numpy as np
from scipy.interpolate import lagrange

coef = np.array([100,0,100])
poly = np.poly1d(coef)
print(poly)

x = np.arange(1,4,1) # x == [1,2,3]
y = poly(x) # y == [200, 500, 1000]
y = list(map(lambda x: x%251, y))
print(y)

poly_intp = lagrange(x, y)
print(poly_intp)
coef_intp = list(map(lambda x: x%251, poly_intp.c))
#coef_intp = [y%251 for y in poly_intp.c]
print(coef_intp)