#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:11:05 2020

@author: josephbattesti
"""
"""
alpha_para : Z
alpha_perp: r
"""
from scipy.sparse import linalg as lina
from scipy.sparse import lil_matrix as lil
import numpy as np

def solve(T1,A,B,C,source):
    "solve A*T=B*T1+C+source"
    d=B.dot(T1.flatten().reshape(-1, 1))+C+source.flatten().reshape(-1,1);
    
    T=lina.spsolve(A,d)
    print(T[5050])
    return T.reshape(T1.shape)

"Heatbath sur deux frontieres, convection et axe de simetrie"
def buildMatrix(Nr,Nz,alpha_para,alpha_perp,deltar,deltat,deltaz,pC,h,Tp):
    N=Nr*Nz;

    "B*T(n+1)=C*T+D"
    B=lil((N,N));
    C=lil((N,N));
    D=lil((N,1))
    
    
    "Construction des Matrices de coefficients Step 1"
    
    for i in range(0,Nr):
        for j in range(0,Nz): 
            
            "Coefficients, dependant du maillage non uniforme"
            b = alpha_perp*deltat/(deltar[i]**2)
            c = alpha_para*deltat/(deltaz[j]**2)
            a = 1+2*b+2*c
            
            pl=i+j*Nr
            "T=Tp"
            if  (i==Nr-1) |  (j==Nz-1):
            
                pc=pl
                'Ces elements ne change pas au cours du temps'
                B[pl,pc]=1;
            
                D[pl,0]=Tp
            
            elif (j==0) :
                
                'indexe de colonne pour la matrice B'
                pc=pl;
                B[pl,pc]=-(3+2*h*deltaz[j]/(alpha_para*pC));
                pc=i+(j+1)*Nr;
                B[pl,pc]=4;
                pc=i+(j+2)*Nr;
                B[pl,pc]=-1;
                

                D[pl,0]=-2*deltaz[j]*h*Tp/(alpha_para*pC);
            
            elif (i==0) :
                pc=pl;
                B[pl,pc]=-3;
                pc=pl+1;
                B[pl,pc]=4;
                pc=pl+2;
                B[pl,pc]=-1;
                
                D[pl,0]=0;
                
            elif (j!=0) and (j!=Nz-1) and (i!=0) and (i!=Nr-1) :
                'indexe de colonne pour la matrice B'
                'termes en i'
                pc=pl;
                B[pl,pc]=a;
                pc=pl+1;
                B[pl,pc]=-b;
                pc=pl-1;
                B[pl,pc]=-b;
                'termes en j'
                pc=i+(j+1)*Nr
                B[pl,pc]=-c;
                pc=i+(j-1)*Nr
                B[pl,pc]=-c;
                'indexe de colonne pour la matrice C'
                'termes en i'
                pc=pl;
                C[pl,pc]=1;

            else : 
                print("missing matrix coefficient")
                
        
        
    B=B.tocsr()
    C=C.tocsr()
    D=D.tocsr()
    
    return B,C,D