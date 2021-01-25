import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


z = np.linspace(0,10,1000)

def integrand(z):

	return 1. / np.sqrt(0.3 * (1 + z)**3 + 0.7)


def integrand_lookback(z):

	return 1. / (np.sqrt(0.3 * (1 + z)**3 + 0.7) * (1 + z))


chi = []
lookback = []
for i in z:
	chi_1, err_1 = quad(integrand, 0, i)
	chi.append(chi_1)
	look_1, err_2 = quad(integrand_lookback, 0, i)
	lookback.append(look_1)

chi = np.array(chi)
lookback = np.array(lookback)

d_a = chi / (1 + z)
d_L = chi * (1 + z)


chi = chi * 2998
d_a = d_a * 2998
d_L = d_L * 2998
lookback = lookback * 2998

hubble = 1. / (np.sqrt(0.3 * (1 + z)**3 + 0.7) * (1 + z))
hubble = z * 2998


plt.figure()
plt.plot(z, chi, label=r'$\chi$')
plt.plot(z, d_a, label=r'$D_A$', linestyle= '--')
plt.plot(z, d_L, label=r'$D_L$', linestyle= '--')
plt.plot(z, lookback, label=r'$D_{LB}$', linestyle='dotted')
plt.plot(z, hubble, label= r'$D_H$', linestyle='dotted')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('z')
plt.ylabel(r'Distance [$h^{-1}$ Mpc]')
plt.xlim(0.05,10)
plt.ylim(1E2,1E4)
plt.legend()
plt.show()