#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ADI as ADI
import utility as ut
import plot_functions as plt
import numpy as np

#Ces paramettres marche pas tant
"Parametres physiques"
rho=8900  #kg.m-3
cSpe=423  #J.Kg-1.K-1
k_para=84 #W.m-1.K-1
k_perp=84 #W.m-1.K-1

alpha_para=k_para/(cSpe*rho)
alpha_perp=k_perp/(cSpe*rho)

Lr=90e-6; #m
Lz=259e-9;#m
duration=100e-5;#s

"Maillage"
deltat=10e-6; #s
deltar=0.3e-6;#m
deltaz=3e-9;#m

# Ca ca marche relativemen Bien
# "Parametres physiques"
# alpha_para=0.5
# alpha_perp=0.5
# Lr=5;
# Lz=5;
# duration=1;
# "Maillage"
# deltat=0.01;
# deltar=0.1;
# deltaz=0.1;

Nt=np.int(np.round(duration/deltat));
Nr=np.int(np.round(Lr/deltar));
Nz=np.int(np.round(Lz/deltaz));

print(Nr,Nz,Nt)

N=Nr*Nz;

"Matrices de coefficients d'un cas simple"
A,B,C,D=ADI.buildMatrices1(Nr, Nz, alpha_para, alpha_perp, deltar, deltat, deltaz)
print("Matrix Done")

"Temperature initiale"
Tini=np.zeros((N,1));

for j in range(0,Nz):
    for i in range(0,Nr): 
        pl=i+j*Nr
        if (i==0) |  (i==Nr-1) |  (j==0) |  (j==Nz-1):
            Tini[pl]=300
        else :
            Tini[pl]=0
    
    
Temperatures=np.zeros((N,Nt)); 
Temperatures[:,0]=Tini[:,0];

"Initialisation du Maillage"
Maille = np.zeros((Nz,Nr,Nt));
Maille[:,:,0]=ut.from1toMatrix(Tini, Nr, Nz)
print("Initial conditions Done")

"Iteration temporelle / Calcul de la solution"
for t in range(0,Nt-1)   :
    T1=Temperatures[:,t]
    T2=ADI.cycle(T1,Nr,Nz,A,B,C,D)
    Temperatures[:,t+1]=T2[:,0]
    Maille[:,:,t+1]=ut.from1toMatrix(T2, Nr, Nz)
    
print("Computation of solution Done")    
    
"Plotting et animation"

"plt.plotFrame(Maille, 0)"
plt.SaveFrames(Maille)
            
"Pour animer les images. telecharger ffmpeg et executer la comande :"
"' ffmpeg -r 30 -i %06d_animation.png vid.mov ' dans un terminal au dossier des images"
            
print("Plotting Done")         
            
            
            
            