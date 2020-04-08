#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import crankNicolson as CrNi
import utility as ut
import numpy as np
import ploting as plt


"Parametres physiques"
rho=8900  #kg.m-3
cSpe=423  #J.Kg-1.K-1
pC=rho*cSpe
k_para=84 #W.m-1.K-1
k_perp=84 #W.m-1.K-1
h=0 #convection
alpha_para=k_para/(pC)
alpha_perp=k_perp/(pC)



"Maillage"
deltar=1e-8;#m
deltaz=1e-8;#m
deltat=1/(4*(alpha_para/(deltar)**2+alpha_perp/(deltaz)**2)); #s

"Dimensions"
Lr=100e-8; #m
Lz=100e-8;#m
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
source=np.zeros((Nz,Nr))

"Matrices de coefficients d'un cranknicolson"
A,B,C=CrNi.buildMatrix1(Nr,Nz, 
                         alpha_para, 
                         alpha_perp, 
                         deltar, deltat, deltaz,
                         pC,source,h)

print("Matrix Done")

"Temperature initiale."
Maille = np.zeros((Nz,Nr,Nt));
for j in range(0,Nz):
    for i in range(0,Nr): 
        pl=i+j*Nr
        if (i==0) |  (i==Nr-1) |  (j==0) |  (j==Nz-1):
            Maille[i,j,0]=300
        else :
            Maille[i,j,0]=0
    

print("Initial conditions Done")

"Iteration temporelle / Calcul de la solution"
for t in range(0,Nt-1)   :
    Maille[:,:,t+1]=CrNi.solve(Maille[:,:,t],A,B,C)
print("Computation of solution Done")    
    
"Plotting et animation"

plt.animate(Maille,Nt)


            
"Pour animer les images. telecharger ffmpeg et executer la comande :"
"' ffmpeg -r 30 -i %06d_animation.png vid.mov ' dans un terminal au dossier des images"
            
print("Plotting Done")         
            
            
            
            