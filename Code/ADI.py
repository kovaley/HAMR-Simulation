#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:50:49 2020

@author: josephbattesti
"""


from scipy.sparse import linalg as lina
import utility as ut
from scipy.sparse import csr_matrix as csr
"""
Ici se trouvent les fonction en lien avec le schéma numerique

La méthode adi se resume comme suit:

Step1
 a * T(i,j,n+1/2) - b * (T(i+1,j,n+1/2)+T(i-1,j,n+1/2))
     = c * T(i,j,n) + d * (T(i,j+1,n)+T(i,j-1,n))
     
         b = alpha_para/deltar^2
         d = alpha_perp/deltaz^2
         a = 2((1/deltat) + b )
         c = 2((1/deltat) - d )
         
Step2

 e * T(i,j,n+1) - d * (T(i,j+1,n+1)+T(i,j-1,n+1))
     = f * T(i,j,n+1/2) + b * (T(i+1,j,n+1/2)+T(i-1,j,n+1/2))
     
         e = 2((1/deltat) + d )
         f = 2((1/deltat) - b )

Pour les deux steps, les equations prennent la forme : B*T(futur)=C*T(passé) ou
B et C sont les matrices des coefficients

-Indexation: i correspond a r et j correspond a z. Su le maillage on indexe : 
    M[j,i]. (PREMIER INDEX est 0 !)
-Voir doc de sparse matrix. Utiliser A.toarray() ou plt.spy(A) pour visualiser

"""

"--------------------------------------------------------------------------------"

"1 cycle ADI. Effectue les deux steps apartir d'une distribution"
"de temperature, dimensions et matrices des coefficients"

def cycle(T1,Nr,Nz,B,C,D,E):
    
    "Step1: Solve B*Ttemp=C*T1=b1"
    b1=C.dot(T1)
    Ttemp=lina.spsolve(B,b1)
    Ttemp=ut.from1to2(Ttemp,Nr,Nz)
    "Step2: Solve B*T2=C*Ttemp=b2"
    b2=E.dot(Ttemp)
    T2=lina.spsolve(D,b2)
    T2=ut.from2to1(T2,Nr,Nz)

    return T2

"Construction des matrices de coefficients pour des CF de type T(froniere)=Tp"

def buildMatrices1(Nr,Nz,alpha_para,alpha_perp,deltar,deltat,deltaz):
    N=Nr*Nz;
    "step 1"
    B=csr((N,N));
    C=csr((N,N));
    "step2"
    D=csr((N,N));
    E=csr((N,N));
    
    "Coefficients"
    b = alpha_para/deltar**2
    d = alpha_perp/deltaz**2
    a = 2*((1/deltat) + b )
    c = 2*((1/deltat) - d )
    e = 2*((1/deltat) + d )
    f = 2*((1/deltat) - b )
    
    "Construction des Matrices de coefficients Step 1"
    
    for i in range(0,Nr):
        for j in range(0,Nz): 
    
            pl=i+j*Nz
            if (i==0) |  (i==Nr-1) |  (j==0) |  (j==Nz-1):
    
                pc=pl
                'Ces elements ne change pas au cours du temps'
                B[pl,pc]=1;
                C[pl,pc]=1;
            else :
    
                'indexe de colonne pour la matrice B'
                pc=pl;
                B[pl,pc]=a;
                pc=pl+1;
                B[pl,pc]=-b;
                pc=pl-1;
                B[pl,pc]=-b;
                'indexe de colonne pour la matrice C'
                pc=pl;
                C[pl,pc]=c;
                pc=i+(j-1)*Nz;
                C[pl,pc]=d;
                pc=i+(j+1)*Nz;
                C[pl,pc]=d;
        
        
    "Construction des Matrices de coefficients Step 2"
    
    "Afin que le systeme forme une matrice tridiagonale on doit changer "
    "l'indexation (pl change). Ainsi, les vecteurs solutions, et temperature "
    "initiale sont indexé differament aux Step1(on utilise alors les fonctions dans Utility "
    
    for j in range(0,Nz):
        for i in range(0,Nr): 
            
            pl=j+i*Nr
     
            if (i==0) |  (i==Nr-1) |  (j==0) |  (j==Nz-1):
    
                pc=pl
                'Ces elements ne change pas au cours du temps'
                D[pl,pc]=1;
                E[pl,pc]=1;
            else :
                'pc indexe de colonne pour la matrice D'
                pc=pl;
                D[pl,pc]=e;
                pc=pl+1;
                D[pl,pc]=-d;
                pc=pl-1;
                D[pl,pc]=-d;
                'pc indexe de colonne pour la matrice E'
                pc=pl;
                E[pl,pc]=f;
                pc=j+(i-1)*Nr;
                E[pl,pc]=b;
                pc=j+(i+1)*Nr;
                E[pl,pc]=b;    
                
    return B,C,D,E

