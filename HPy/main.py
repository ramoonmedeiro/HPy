from specials import Psi
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# COLOR STEP

BOLD = '\033[1m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'

# MAIN FUNCTION


banner = '''
		   \u001b[36m


 	   '##::::'##:'########::'##:::'##:
	    ##:::: ##: ##.... ##:. ##:'##::
 	    ##:::: ##: ##:::: ##::. ####:::
 	    #########: ########::::. ##::::
	    ##.... ##: ##.....:::::: ##::::
	    ##:::: ##: ##::::::::::: ##::::
	    ##:::: ##: ##::::::::::: ##::::
	   ..:::::..::..::::::::::::..::::: v1.0

		       \u001b[0m

	       \033[1;34m   *- coded by RAMON\033[m

'''

print(banner)

while(True):
	try:
		print(BOLD + '         \033[1;32m-MENU-\033[m    ')
		print(BOLD + '[1] Radial Wave Function')
		print(BOLD + '[2] Angular Wave Function')
		print(BOLD + '[3] Exit')

		choice = int(input(BOLD + 'CHOICE: '))


		if choice == 1:
			print()
			print(BOLD + '   \033[1;32m*-RADIAL SELECTED-*\033[m\n')
			n = int(input(BOLD + 'Value for N: '))
			l = int(input(BOLD + 'Value for L: '))
			print(BOLD + 'Wait...\n')

			r = np.linspace(0, 10, 100)
			R = Psi.radial(r, n, l)

			fig = plt.figure(figsize=(10,10))

			# FIRST GRAPH
			#fig.add_subplot(211)

			sns.lineplot(r, R, linewidth=3, c='black')
			#plt.ylabel(f'$R_{n},_{l}(r)$', fontsize=25)
			##plt.axhline(linewidth=2, linestyle="--", color='r')
			#plt.grid('True')
			#plt.xlim(0.0, 10.0)


			# SECOND GRAPH
			fig.add_subplot(212)
			plt.plot(r, (R**2)*(r**2), linewidth=3, c='black')
			plt.xlabel('$r [a_0]$',fontsize=25)
			plt.ylabel(f'$[R_{n},_{l}(r)]^{2}r^{2}$', fontsize=25)
			plt.axhline(linewidth=2, linestyle="--", color='r')
			plt.grid('True')
			plt.xlim(0.0, 10.0)


			# SHOW FIG
			plt.show()
			print()

		elif choice == 2:
			print()
			print(BOLD + '   \033[1;32m*-ANGULAR SELECTED-*\033[m\n')
			l = int(input(BOLD + 'Value for L: '))
			m = int(input(BOLD + 'Value for M: '))
			print(BOLD + 'Wait...\n')

			phi = np.linspace(0, np.pi, 100)
			theta = np.linspace(0, 2*np.pi, 100)
			phi, theta = np.meshgrid(phi, theta)

			Ylm = Psi.angular(m, l, theta, phi)		

			# SPHERICAL TO XYZ
			R = abs(Ylm)
			x = R * np.sin(phi) * np.cos(theta)
			y = R * np.sin(phi) * np.sin(theta)
			z = R * np.cos(phi)

			# Plot the surface
			cmap = plt.get_cmap('twilight_shifted')
			N = mcolors.Normalize(vmin=z.min(), vmax=z.max()) # NORMALIZATION OF Ylm


			fig = plt.figure(figsize=(10,10))
			ax = fig.add_subplot(111, projection='3d')
			ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('twilight_shifted'), facecolors=cmap(N(R)), lw = 0, antialiased=True)
			ax.set_title(fr'$Y_{l}^{m}(\theta, \phi)$', fontsize=20)
			ax.set_xlabel(r'$x$', fontsize=13)
			ax.set_ylabel(r'$y$', fontsize=13)
			ax.set_zlabel(r'$z$', fontsize=13)

			plt.show()


		elif choice == 3:
			print(BOLD + 'Good Bye!!')
			break
		else:
			print()
	except (EOFError, KeyboardInterrupt):
		print()
		print(BOLD + 'OOOPS, \033[1;31mINTERRUPTION!!\033[m')
		break