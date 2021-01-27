import numpy as np
import matplotlib.pyplot as plt


omega_m = np.linspace(0,1.6,50)
omega_lambda = 0.5 * omega_m 
flat = 1 - omega_m
plt.figure()
plt.plot(omega_m, omega_lambda, linestyle = '--')
plt.plot(omega_m, flat, linestyle = '--')
plt.text(0.2, 0.6, 'Flat Universe', rotation=-30)
plt.text(0.9, 0.3, 'Decelerating Universe', rotation=15)
plt.text(0.9, 0.5, 'Accelerating Universe', rotation=15)
plt.xlabel(r'$\Omega_m$')
plt.ylabel(r'$\Omega_{\Lambda}$')
plt.title('CDM Constraints')
plt.xlim(0,1.6)
plt.ylim(0,2.3)
plt.show()