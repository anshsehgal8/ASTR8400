import numpy as np
import matplotlib.pyplot as plt

h = 6.626E-27
c = 2.99E10
k = 1.38E-16
T = 2.728

def configure_matplotlib(hardcopy=False):
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.rc('axes', labelsize=8)
    plt.rc('legend', fontsize=8)
    plt.rc('font', family='Times New Roman' if hardcopy else 'DejaVu Sans', size=8)
    plt.rc('text', usetex=hardcopy)


configure_matplotlib(hardcopy=True)


nu = np.linspace(6.7E10,6.9E11,500)

boltzmann = np.exp((h * nu) / (k * T))

B_v = (2 * h * nu**3 / c**2 ) / (boltzmann - 1)

B_v = B_v * 1E17
nu = nu / (29.9792458 * 1E9)

plt.figure()
plt.plot(nu, B_v)
plt.xlabel(r'Frequency (cm$^{-1}$)')
plt.ylabel(r'Brightness (MJy/str)')
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Blackbody Spectrum of the CMB ($T_0$ = 2.728 K)')
plt.show()