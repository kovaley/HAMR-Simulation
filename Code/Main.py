#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import euler_Implicite as euImp
import numpy as np
import ploting as plt
import time
import Terme_Source as TS
import nu_grid as nu_grid

"Parametres physiques"
rho=8900  #kg.m-3
cSpe=423  #J.Kg-1.K-1
pC=rho*cSpe
k_para=84 #W.m-1.K-1
k_perp=84 #W.m-1.K-1
h=10 #convection
alpha_para=k_para/(pC)
alpha_perp=k_perp/(pC)
Tp=300
Tini=300
P_las=1e-3

"Pas de temps"
deltat=1e-9

"Dimensions"

Nt=200;
Nr=200;
Nz=200;


duration=Nt*deltat;#s
"Maillage"
a=10
k=300e-9 #Domaine de simulation
# r_pos, z_pos, deltar,deltaz=nu_grid.get_grid(Nr,Nz,a,k);
r_pos = k/Nr*np.arange(Nr+1)
z_pos = k/Nz*np.arange(Nz+1)
deltar = k/Nr*np.ones(Nr)
deltaz = k/Nz*np.ones(Nz)
 
print(Nr,Nz,Nt)

N=Nr*Nz;


"Matrices de coefficients d'un cranknicolson"
A,B,C=euImp.buildMatrix(Nr,Nz, 
                         alpha_para, 
                         alpha_perp, 
                         deltar, deltat, deltaz,
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
    
"Plotting et animation"

plt.animate(Maille,Nt)
plt.animate(source,Nt)


print("Plotting Done")         


          
            
            
            