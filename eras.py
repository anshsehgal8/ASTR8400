import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(1E-5, 1, 500)

rho_rad  = 1E-4 * a**(-4)
rho_m    = 0.3 * a**(-3)
rho_dark = 0.7 * a / a

plt.figure()
plt.plot(a,rho_rad,  label='Radiation')
plt.plot(a,rho_m,    label='Matter')
plt.plot(a,rho_dark, label='Cosm. Const.')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1E-5,1)
plt.ylim(1E-4,1E13)
plt.xlabel('Scale factor a')
plt.ylabel(r'$\rho / \rho_c$')
plt.legend(loc='upper right')
plt.show()