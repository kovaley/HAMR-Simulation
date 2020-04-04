#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import crankNicolson as CrNi
import utility as ut
import plot_functions as plt
import numpy as np


"Parametres physiques"
rho=8900  #kg.m-3
cSpe=423  #J.Kg-1.K-1
pC=rho*cSpe
k_para=84 #W.m-1.K-1
k_perp=84 #W.m-1.K-1
h=0 #convection
alpha_para=k_para/(pC)
alpha_perp=k_perp/(pC)

"Dimensions"
Lr=100e-8; #m
Lz=100e-8;#m
duration=100e-5;#s

"Maillage"
deltat=10e-6; #s
deltar=1e-7;#m
deltaz=1e-7;#m

Nt=np.int(np.round(duration/deltat));
Nr=np.int(np.round(Lr/deltar));
Nz=np.int(np.round(Lz/deltaz));

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

"Temperature initiale. Ensuite Ttemp s'actualise a chaque iteration"
Ttemp=np.zeros((N,1));

for j in range(0,Nz):
    for i in range(0,Nr): 
        pl=i+j*Nr
        if (i==0) |  (i==Nr-1) |  (j==0) |  (j==Nz-1):
            Ttemp[pl]=300
        else :
            Ttemp[pl]=0
    

"Initialisation du Maillage"
Maille = np.zeros((Nz,Nr,Nt));
Maille[:,:,0]=ut.VectorToMatrix(Ttemp, Nr, Nz)
print("Initial conditions Done")

"Iteration temporelle / Calcul de la solution"
for t in range(0,Nt-1)   :
    T2=CrNi.solve(Ttemp,A,B,C)
    Ttemp[:,0]=T2
    Maille[:,:,t+1]=ut.VectorToMatrix(T2, Nr, Nz)
    
print("Computation of solution Done")    
    
"Plotting et animation"

"plt.plotFrame(Maille, 0)"
plt.SaveFrames(Maille)
            
"Pour animer les images. telecharger ffmpeg et executer la comande :"
"' ffmpeg -r 30 -i %06d_animation.png vid.mov ' dans un terminal au dossier des images"
            
print("Plotting Done")         
            
            
            
            