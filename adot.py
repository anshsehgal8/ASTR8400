import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


z = np.linspace(0,3,1000)

H_z = np.sqrt(0.3 * (1 + z)**3 + 0.7)

adot = 68  * H_z / (1 + z)

plt.figure()
plt.plot(z, adot, label= r'$\dot{a}(z)$')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('z')
plt.ylabel(r'$\dot{a}$  [$h^{-1}$ Mpc]')
plt.xlim(0,2.5)
plt.ylim(54,76)
plt.legend()
plt.show()