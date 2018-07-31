import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import lagrange

neg_bound = -10
pos_bound = 10

#group_size = 4
group_size = input('please enter the group size:')
group_size = int(group_size)

# generate the random polynomial (the secret to be shared)
rd_coef = np.random.randint(1, 10, group_size)
poly = np.poly1d(rd_coef)
print(poly)

#devs = np.random.randn(group_size)
devs = np.linspace(neg_bound,pos_bound,group_size)
print('device:',devs)
# plot the origin polynomial for this authentication
x = np.linspace(neg_bound,pos_bound,100)
y = poly(x)

fig, axes = plt.subplots(nrows=2,ncols=2)

axes[0,0].plot(x, y, 'b--')
axes[0,1].plot(x, y, 'b--')

# compute devices' secret tokens
tokens = np.array([poly(d) for d in devs])
#tokens = np.array(list(map(poly, devs)))
axes[0,0].plot(devs, tokens, 'r*', markersize = 12)
axes[1,0].plot(devs, tokens, 'r*', markersize = 12)


print('tokens:',tokens)

poly_p = lagrange(devs, tokens)
print(poly_p)
x_p = np.linspace(neg_bound,pos_bound,100)
y_p = poly_p(x_p)
axes[0,0].plot(x_p, y_p, 'y')
axes[1,1].plot(x_p, y_p, 'y')
fig.legend(['polynomial', 'devices', 'lagrange interpolation'], loc='upper left')
plt.show()