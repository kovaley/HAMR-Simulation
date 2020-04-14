#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import crankNicolson as CrNi
import numpy as np
import ploting as plt
import time
import Terme_Source as TS

"Parametres physiques"
rho=8900  #kg.m-3
cSpe=423  #J.Kg-1.K-1
pC=rho*cSpe
k_para=84 #W.m-1.K-1
k_perp=84 #W.m-1.K-1
h=100 #convection
alpha_para=k_para/(pC)
alpha_perp=k_perp/(pC)
Tp=273
Tini=300
P_las=1000

"Maillage"
deltar=1e-8;#m
deltaz=1e-8;#m
deltat=1/(4*(alpha_para/(deltar)**2+alpha_perp/(deltaz)**2)); #s

"Dimensions"
Lr=100e-9; #m
Lz=100e-9;#m
duration=100*deltat;#s

Nt=np.int(np.round(duration/deltat));
Nr=np.int(np.round(Lr/deltar));
Nz=np.int(np.round(Lz/deltaz));

"Condition de stabilité"
crit=deltat*(alpha_para/(deltar)**2+alpha_perp/(deltaz)**2)
if crit>0.5:
    print("big, ça sera pas stable")

    
print(Nr,Nz,Nt)

N=Nr*Nz;
source=np.zeros((Nz,Nr,Nt))


"Matrices de coefficients d'un cranknicolson"
A,B,C=CrNi.buildMatrix(Nr,Nz, 
                         alpha_para, 
                         alpha_perp, 
                         deltar, deltat, deltaz,
                         pC,source,h,Tp)

print("Matrix Done")

"Temperature initiale."
Maille = np.zeros((Nz,Nr,Nt));
Maille[:,:,0]=Tini

    

print("Initial conditions Done")
startime = time.time()
"Iteration temporelle / Calcul de la solution"
for t in range(0,Nt-1)   :
    Maille[:,:,t+1]=CrNi.solve(Maille[:,:,t],A,B,C)
#    source[:,:,t]=TS.SourceCreation(deltar, deltaz, Nr, Nz, t*deltat, P_las)
    
execution_time = time.time()-startime 
print("Computation of solution done in {:.2f} seconds".format(execution_time))
    
"Plotting et animation"

plt.animate(Maille,Nt)
#plt.animate(source,Nt)


            
"Pour animer les images. telecharger ffmpeg et executer la comande :"
"' ffmpeg -r 30 -i %06d_animation.png vid.mov ' dans un terminal au dossier des images"
            
print("Plotting Done")         


          
            
            
            