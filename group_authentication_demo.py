import numpy as np
from scipy.interpolate import lagrange

group_size = 20

# generate the random polynomial (the secret to be shared)
rd_coef = np.random.randint(1, 10, group_size)
poly = np.poly1d(rd_coef)
print(poly)

# multiples of 10 resemble 10 different devices
devs = np.random.randn(group_size)
print('device:',devs)

# compute devices' secret tokens
tokens = np.array([poly(d) for d in devs])
#tokens = np.array(list(map(poly, devs)))

print('tokens:',tokens)

poly_p = lagrange(devs, tokens)
print(poly_p)