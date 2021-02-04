import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import scipy.stats
import statistics 




z, mu_obs, error = np.loadtxt('dmr_data.csv', delimiter=',', skiprows=1, unpack=True)


mu_obs = np.array(mu_obs)
mu_obs += 19.365


def calc_mu(omega_m, omega_lambda):
	
	def integrand(z):

		return 1. / np.sqrt(omega_m * (1 + z)**3 + omega_lambda)


	chi = []

	for i in z:
		chi_1, err_1 = quad(integrand, 0, i)
		chi.append(chi_1)

	chi = np.array(chi)


	units = 2998 * 1E6 / 0.7

	d_L = chi * (1 + z)
	d_L *= units

	mu =  5 * (np.log10(d_L) - 1)


	residual = mu_obs - mu 
	variance = statistics.variance(mu_obs)
	chi_sq  = np.sum(residual**2 / variance) / 3
	chi_sq = round(chi_sq, 2)
	return mu, residual, chi_sq

mu_fitted, residual_fitted, chi_sq_fitted = calc_mu(0.26,0.74)
mu_naive,  residual_naive,  chi_sq_naive  = calc_mu(1.0,0.0)

fig = plt.figure(figsize=[8,6])
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(2,2,2)
ax4 = fig.add_subplot(2,2,4)
ax1.plot(z, mu_obs, marker='o', color='black', label='SN1a Pantheon')
ax1.plot(z, mu_fitted, label=r'$\Omega_{\Lambda}$ = 0.74, $\Omega_m$ = 0.26')
text1 = r'$\chi^2$ / $\nu$ = {}'.format(chi_sq_fitted)
ax1.text(0.012,42, text1)
ax1.set_xscale('log')
ax1.set_ylim(33,47)
ax2.errorbar(z, residual_fitted, yerr=error, fmt = 'ko')
ax2.set_xscale('log')
ax2.set_ylim(-0.8,0.8)
ax1.set_ylabel('Distance Modulus(mag)')
ax2.set_xlabel('z')
ax2.set_ylabel('Residual')
ax1.set_title('Hubble Diagram for Pantheon Sample')
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.legend()



ax3.plot(z, mu_obs, marker='o', color='black', label='SN1a Pantheon')
ax3.plot(z, mu_naive, label=r'$\Omega_{\Lambda}$ = 0')
text2 = r'$\chi^2$ / $\nu$ = {}'.format(chi_sq_naive)
ax3.text(0.012,42, text2)
ax3.set_xscale('log')
ax3.set_ylim(33,47)
#ax3.set_ylabel('Distance Modulus(mag)')
ax3.set_title('Hubble Diagram for Pantheon Sample')
ax3.legend()
ax4.errorbar(z, residual_naive, yerr=error, fmt = 'ko')
ax4.set_xscale('log')
ax4.set_ylim(-0.8,0.8)
ax4.set_xlabel('z')
#ax4.set_ylabel('Residual')
plt.setp(ax3.get_xticklabels(), visible=False)
plt.subplots_adjust(right=0.96,left=0.10, bottom=0.10, top=0.94, hspace=0.13)
plt.show()
