#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ADI as ADI
import utility as ut
import plot_functions as plt
import numpy as np

"Parametres physiques"
alpha_para=0.5
alpha_perp=0.5
Lr=5;
Lz=5;
duration=1;
"Maillage"
deltat=0.01;
deltar=0.1;
deltaz=0.1;

Nr=np.int(np.round(Lr/deltar));
Nz=np.int(np.round(Lz/deltaz));
Nt=np.int(np.round(duration/deltat));
N=Nr*Nz;

"Matrices de coefficients d'un cas simple"
A,B,C,D=ADI.buildMatrices1(Nr, Nz, alpha_para, alpha_perp, deltar, deltat, deltaz)

"Temperature initiale"
Tini=np.zeros((N,1));

for j in range(0,Nz):
    for i in range(0,Nr): 
        pl=i+j*Nr
        if (i==0) |  (i==Nr-1) |  (j==0) |  (j==Nz-1):
            Tini[pl]=100
        else :
            Tini[pl]=0
    
    
Temperatures=np.zeros((N,Nt)); 
Temperatures[:,0]=Tini[:,0];

"Initialisation du Maillage"
Maille = np.zeros((Nz,Nr,Nt));
Maille[:,:,0]=ut.from1toMatrix(Tini, Nr, Nz)

"Iteration temporelle / Calcul de la solution"
for t in range(0,Nt-1)   :
    T1=Temperatures[:,t]
    T2=ADI.cycle(T1,Nr,Nz,A,B,C,D)
    Temperatures[:,t+1]=T2[:,0]
    Maille[:,:,t+1]=ut.from1toMatrix(T2, Nr, Nz)
    
"Plotting et animation"

plt.plotFrame(Maille, 0)
plt.SaveFrames(Maille)
            
"Pour animer les images. telecharger ffmpeg et executer la comande :"
"' ffmpeg -r 30 -i %06d_animation.png vid.mov ' dans un terminal au dossier des images"
            
        
            
            
            
            