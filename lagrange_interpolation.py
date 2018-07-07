from scipy.interpolate import lagrange
import numpy as np

x = np.array([-1, 0, 1, 2])
w = np.array([3, -4, 5, -6])

poly = lagrange(x,w)
print(poly)
print(poly.coef)