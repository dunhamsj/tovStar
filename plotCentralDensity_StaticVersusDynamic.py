#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use( 'publication.sty' )

nN = '03'

ID = [  f'StaticTOV_nN{nN}_nX032_NoSL', \
        f'StaticTOV_nN{nN}_nX048_NoSL', \
        f'StaticTOV_nN{nN}_nX064_NoSL', \
       f'DynamicTOV_nN{nN}_nX032_NoSL', \
       f'DynamicTOV_nN{nN}_nX048_NoSL', \
       f'DynamicTOV_nN{nN}_nX064_NoSL' ]
ID = [  f'StaticTOV_nN{nN}_nX032', \
        f'DynamicTOV_nN{nN}_nX032' ]

# colorblind-friendly palette: https://gist.github.com/thriveth/8560036
color = ['#377eb8', '#ff7f00', '#4daf4a', \
         '#f781bf', '#a65628', '#984ea3', \
         '#999999', '#e41a1c', '#dede00']

n2 = -1
n3 = -1
k  = 0
for i in range( len( ID ) ):

    t, rhoC = np.loadtxt( '{:}_CentralDensityVersusTime.dat'.format( ID[i] ) )

    if ( 'Dynamic' in ID[i] ) :
      ls = '--'
      n3 += 1
      c = n3
    else :
      ls = '-'
      n2 += 1
      c = n2

    plt.plot( t, 1.0e4 * ( rhoC - rhoC[0] ) / rhoC[0], c = color[c], ls = ls, \
              label = r'$\texttt{{{:}}}$'.format( ID[i] ) )

#plt.title( 'No Slope Limiter' )
plt.xlabel( r'$t/\mathrm{ms}$' )
plt.ylabel( r'$10^{4}\times\left(\bar{\rho}_{<1\,\mathrm{km}}\left(t\right)-\bar{\rho}_{<1\,\mathrm{km}}\left(0\right)\right)/\bar{\rho}_{<1\,\mathrm{km}}\left(0\right)$' )
plt.legend()
plt.grid()

plt.show()

#figName = f'/home/kkadoogan/fig.TOV_StaticVersusDynamic_nN{nN}.png'
#plt.savefig( figName, dpi = 300 )
#print( '\n  Saved {:}'.format( figName ) )
