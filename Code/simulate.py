#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:59:28 2020

@author: josephbattesti
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import euler_Implicite as euImp
import numpy as np
import ploting as plt
import time
import Terme_Source as TS
import nu_grid as nu_grid



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

def simulate(P_las,deltaz,deltar,deltat,Lr,Lz,duration):
    
    "Parametres physiques"
    rho=8900  #kg.m-3
    cSpe=423  #J.Kg-1.K-1
    pC=rho*cSpe
    k_para=84 #W.m-1.K-1
    k_perp=84 #W.m-1.K-1

    h=10 #convection
    Tp=300
    Tini=300

    alpha_para=k_para/(pC)
    alpha_perp=k_perp/(pC)
    "pas"
    Nr=int(np.round(Lr/deltar))
    Nz=int(np.round(Lz/deltaz))
    Nt=int(np.round(duration/deltat))
    "Positions"
    r_pos = deltar*np.arange(Nr+1)
    z_pos = deltat*np.arange(Nz+1)
    "Vecteur pas"
    dr_vec = deltar*np.ones(Nr)
    dz_vec = deltaz*np.ones(Nz)
    
    
    print(Nr,Nz,Nt)
    
    "Matrices de coefficients"
    A,B,C=euImp.buildMatrix(Nr,Nz, 
                         alpha_para, 
                         alpha_perp, 
                         dr_vec, deltat, dz_vec,
                         pC,h,Tp)

    print("Matrix Done")
    
    "Temperature initiale."
    Maille = np.zeros((Nz,Nr,Nt));
    Maille[:,:,0]=Tini
    source=np.zeros((Nz,Nr,Nt))
        
    print("Initial conditions Done")
              
    startime = time.time()
    "Iteration temporelle / Calcul de la solution"
    for t in range(0,Nt-1)    :
        source[:,:,t]=deltat*TS.SourceCreation(r_pos, z_pos, Nr,
                                                Nz, t*deltat, P_las)/pC
        
        Maille[:,:,t+1]=euImp.solve(Maille[:,:,t],A,B,C,source[:,:,t])
        
    execution_time = time.time()-startime 
    print("Computation of solution done in {:.2f} seconds".format(execution_time))
    
    return Maille
    
P_las=10**np.arange(3)*1e-3   #W  
resultats=[]

print(len(P_las))

for n in range(0,len(P_las)):
    resultats.append(simulate(P_las[n],deltaz,deltar,deltat,Lr,Lz,duration))


"Plotting et animation"

plt.animate(resultats[0])
plt.animate(resultats[1])
# plt.animate(source,Nt)


print("Plotting Done")   



