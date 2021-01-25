import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


z = np.linspace(0,10,100)

def integrand(z):

	return 1. / np.sqrt(0.3 * (1 + z)**3 + 0.7)


chi = []
for i in z:
	chi_1, err_1 = quad(integrand, 0, i)
	chi.append(chi_1)

chi = np.array(chi)

d_a = chi / (1 + z)
d_L = chi * (1 + z)


chi = chi * 2800
d_a = d_a * 2800
d_L = d_L * 2800

plt.figure()
plt.plot(z, chi, label=r'$\chi$')
plt.plot(z, d_a, label=r'$d_A$')
plt.plot(z, d_L, label=r'$d_L$')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('z')
plt.ylabel(r'Distance [$h^{-1}$ Mpc]')
plt.xlim(0,10)
plt.ylim(100,10000)
plt.legend()
plt.show()