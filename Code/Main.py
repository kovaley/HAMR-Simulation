#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import euler_Implicite as euImp
import crankNicolson as CR
import numpy as np
import ploting as plt
import time
import Terme_Source as TS
import nu_grid as nu_grid
from scipy.sparse import linalg as lina
from scipy.sparse import lil_matrix as lil


"Parametres physiques"
rho=8900  #kg.m-3
cSpe=423  #J.Kg-1.K-1
pC=rho*cSpe
k_para=84 #W.m-1.K-1
k_perp=84 #W.m-1.K-1
h=10 #convection
alpha_para=k_para/(pC)
alpha_perp=k_perp/(pC)
Tp=0
Tini=0
P_las=1e-3

"Pas de temps"
deltat=1e-9

"Dimensions"

Nt=100;
Nr=100;
Nz=100;


duration=Nt*deltat;#s
"Maillage"
a=10
k=100e-9 #Domaine de simulation
# r_pos, z_pos, deltar,deltaz=nu_grid.get_grid(Nr,Nz,a,k);
r_pos = k/Nr*np.arange(Nr+1)
z_pos = k/Nz*np.arange(Nz+1)
deltar = k/Nr*np.ones(Nr)
deltaz = k/Nz*np.ones(Nz)

# deltat=1/(4*(alpha_para/(deltar)**2+alpha_perp/(deltaz)**2)); #s


# "Condition de stabilité"
# crit=deltat*(alpha_para/(deltar)**2+alpha_perp/(deltaz)**2)
# if crit>0.5:
#     print("big, ça sera pas stable")
 
# print(Nr,Nz,Nt)

N=Nr*Nz;


"Matrices de coefficients d'un cranknicolson"
A,B,C=CR.buildMatrix1(Nr,Nz, 
                         alpha_para, 
                         alpha_perp, 
                         deltar, deltat, deltaz,
                         pC,h,Tp)

print("Matrix Done")

"Temperature initiale."
Maille = np.zeros((Nz,Nr,Nt));
Maille[:,:,0]=Tini

source=np.zeros((Nz,Nr,Nt))
for t in range(0,Nt-1)   :
    for i in range(0,Nr-1) :
        for j in range(0,Nz-1) :
            if (j>50) :
                source[j,i,t]=20
    
source1=source[:,:,0]
source1=source1.flatten().reshape(-1,1)
mailloche=Maille[:,:,0].flatten().reshape(-1, 1)
d=B.dot(Maille[:,:,0].flatten().reshape(-1, 1))+C+source1.flatten().reshape(-1,1);
T=np.linalg.solve(A,d)
soletgoblet=T.reshape(Maille[:,:,0].shape)    
print("Initial conditions Done")

#startime = time.time()
#"Iteration temporelle / Calcul de la solution"
#for t in range(0,Nt-1)    :
#    # source[:,:,t]=deltat*TS.SourceCreation(r_pos, z_pos, Nr,
#                                            # Nz, t*deltat, P_las)/pC
#    
#    Maille[:,:,t+1]=CR.solve(Maille[:,:,t],A,B,C,source[:,:,t])
#    
#    
#execution_time = time.time()-startime 
#print("Computation of solution done in {:.2f} seconds".format(execution_time))
#    
#"Plotting et animation"
#
#plt.animate(Maille,Nt)
## plt.animate(source,Nt)
#

print("Plotting Done")         


          
            
            
            