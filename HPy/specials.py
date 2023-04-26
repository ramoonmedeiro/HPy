import scipy.special as spe
import numpy as np


class Psi():
	def __init__(self, r, n, l):
		self.r = r
		self.n = n
		self.l = l

	# LAGUERRE FUNCTIONS
	def radial(r, n, l):
		coeff = np.sqrt((2/n)**3*spe.factorial(n-l-1)/(2*n*spe.factorial(n+l)))
		laguerre = spe.assoc_laguerre(2*r/n, n-l-1, 2*l+1)
		full = coeff * np.exp(-r/n) * (2*r/n)**l * laguerre

		return full

	# SPHERICAL HARMONICS
	def angular(m, l, theta, phi):
		Ylm = spe.sph_harm(m, l, theta, phi).real

		return Ylm

'''
if __name__ == '__main__':
	pass
'''