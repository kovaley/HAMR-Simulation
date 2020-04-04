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

def solve(T1,A,B,C):
    "solve A*T=B*T1+C"
    d=B.dot(T1)+C;
    T=lina.spsolve(A,d)
    
    return T

"Heatbath sur deux frontieres, convection et axe de simetrie"
def buildMatrix(Nr,Nz,alpha_para,alpha_perp,deltar,deltat,deltaz,pC,source,h):
    N=Nr*Nz;

    "B*T(n+1)=C*T+D"
    B=lil((N,N));
    C=lil((N,N));
    D=lil((N,1))
    
    "Coefficients"
    b = alpha_perp*deltat/(2*deltar**2)
    c = alpha_para*deltat/(2*deltaz**2)
    a = 1+b+c
    d= 1-b-c
    S=source*deltat/pC
    "Construction des Matrices de coefficients Step 1"
    
    for i in range(0,Nr):
        for j in range(0,Nz): 
        
            pl=i+j*Nr
            "T=Tp"
            if  (i==Nr-1) |  (j==Nz-1):
            
                pc=pl
                'Ces elements ne change pas au cours du temps'
                B[pl,pc]=1;
                C[pl,pc]=1;
                " D[pl,0]=S[j,i]" "faut-il ajouter S aux fontieres ?"
            
            elif (j==0) :
                
                'indexe de colonne pour la matrice B'
                pc=pl;
                B[pl,pc]=-(3+h/(alpha_para*pC));
                pc=pl+1;
                B[pl,pc]=4;
                pc=pl+2;
                B[pl,pc]=-1;
                
                pc=pl;
                D[pl,pc]=-deltaz*h/(alpha_para*pC);
            
            elif (i==0) :
                pc=pl;
                B[pl,pc]=-3;
                pc=pl+1;
                B[pl,pc]=4;
                pc=pl+2;
                B[pl,pc]=-1;
            
            else :
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
                C[pl,pc]=d;
                pc=pl+1;
                C[pl,pc]=b;
                pc=pl-1;
                C[pl,pc]=b;
                'termes en j'
                pc=i+(j+1)*Nr
                C[pl,pc]=c;
                pc=i+(j-1)*Nr
                C[pl,pc]=c;
                'Source'
                D[pl,0]=S[j,i]
                
        
        
    B=B.tocsr()
    C=C.tocsr()
    D=D.tocsr()
    
    return B,C,D

"Heat bath sur les 4 frontieres"
def buildMatrix1(Nr,Nz,alpha_para,alpha_perp,deltar,deltat,deltaz,pC,source,h):
    N=Nr*Nz;

    "B*T(n+1)=C*T+D"
    B=lil((N,N));
    C=lil((N,N));
    D=lil((N,1));
    
    "Coefficients"
    b = alpha_perp*deltat/(2*deltar**2)
    c = alpha_para*deltat/(2*deltaz**2)
    a = 1+b+c
    d = 1-b-c
    "Construction des Matrices de coefficients Step 1"
    
    for i in range(0,Nr):
        for j in range(0,Nz): 
        
            pl=i+j*Nr
            "T=Tp"
            if (i==0) |  (i==Nr-1) |  (j==0) |  (j==Nz-1):
                pc=pl
                'Ces elements ne change pas au cours du temps'
                B[pl,pc]=1;
                C[pl,pc]=1;
            
            else :
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
                C[pl,pc]=d;
                pc=pl+1;
                C[pl,pc]=b;
                pc=pl-1;
                C[pl,pc]=b;
                'termes en j'
                pc=i+(j+1)*Nr
                C[pl,pc]=c;
                pc=i+(j-1)*Nr
                C[pl,pc]=c;
                
        
        
    B=B.tocsr()
    C=C.tocsr()
    D=D.tocsr()
    
    return B,C,D