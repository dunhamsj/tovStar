#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use( 'publication.sty' )

ID = [ 'StaticTOV_nN02_nX032', \
       'StaticTOV_nN02_nX048', \
       'StaticTOV_nN02_nX064', \
       'StaticTOV_nN03_nX032', \
       'StaticTOV_nN03_nX048', \
       'StaticTOV_nN03_nX064' ]

ID = [ 'DynamicTOV_nN02_nX032', \
       'DynamicTOV_nN02_nX048', \
       'DynamicTOV_nN02_nX064', \
       'DynamicTOV_nN03_nX032', \
       'DynamicTOV_nN03_nX048', \
       'DynamicTOV_nN03_nX064' ]

# colorblind-friendly palette: https://gist.github.com/thriveth/8560036
color = ['#377eb8', '#ff7f00', '#4daf4a', \
         '#f781bf', '#a65628', '#984ea3', \
         '#999999', '#e41a1c', '#dede00']

n2 = -1
n3 = -1
k  = 0
for i in range( len( ID ) ):

    t, rhoC = np.loadtxt( '{:}_CentralDensityVersusTime.dat'.format( ID[i] ) )

    if ( 'nN03' in ID[i] ) :
      ls = '--'
      n3 += 1
      c = n3
    else :
      ls = '-'
      n2 += 1
      c = n2

    plt.plot( t, 1.0e4 * ( rhoC - rhoC[0] ) / rhoC[0], \
              c = color[c], ls = ls, \
              label = r'$\texttt{{{:}}}$'.format( ID[i] ) )

plt.xlabel( r'$t/\mathrm{ms}$' )
plt.ylabel( r'$10^{4}\times\Delta\rho_{\mathrm{c}}/\rho_{\mathrm{c}}$' )
plt.legend()
plt.grid()

#plt.show()

figName = '/home/kkadoogan/fig.TOV_VaryPolynomialDegree_Dynamic.png'
plt.savefig( figName, dpi = 300 )
print( '\n  Saved {:}'.format( figName ) )
