#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import euler_Implicite as euImp
import numpy as np
import ploting as plt
import time
import Terme_Source as TS
import nu_grid as nu_grid
import simulate as simulate
import matplotlib.pyplot as plot
"constants"
Tcurie=1394 #K
sampling_depth=9 #cellules

"Dimensions"
Lr=300e-9
Lz=300e-9
duration=50e-9
"Nombre de celulles"
deltat=0.5e-9;
deltar=3e-9;
deltaz=3e-9;


Nr=int(np.round(Lr/deltar))
Nz=int(np.round(Lz/deltaz))
Nt=int(np.round(duration/deltat))


P_las=10**np.arange(1)*1e-3   #W  
resultats=[]
rayonbit=[]
print(len(P_las))

for n in range(0,len(P_las)):
    resultats.append(simulate.simulate(P_las[n],deltaz,deltar,deltat,Lr,Lz,duration))
    rayonbit.append(deltar*np.sum(resultats[n][:,sampling_depth,:]>Tcurie,axis=0))

"Plotting et animation"
plot.plot(deltat*np.arange(0,Nt),rayonbit[0])

#plt.animate(resultats[0])
#plt.animate(resultats[1])
# plt.animate(source,Nt)


print("Plotting Done")   


          
            
            
            