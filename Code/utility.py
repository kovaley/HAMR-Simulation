#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

"vecteur en step1 reordonée en step2"

def from1to2(vector,Nr,Nz):
    a=vector.copy()
    newVector=np.zeros((Nr*Nz,1))
    
    for i in range(0,Nr):
        for j in range(0,Nz):
            pl1=i+j*Nz
            pl2=j+i*Nr

            newVector[pl2]=a[pl1]
    return newVector

"step2 to step1"
def from2to1(vector,Nr,Nz):
    a=vector.copy()
    newVector=np.zeros((Nr*Nz,1))
    
    for i in range(0,Nr):
        for j in range(0,Nz):
            pl1=i+j*Nz
            pl2=j+i*Nr
            newVector[pl1]=a[pl2]
    return newVector

"Vecteur des temperature (step1) to maillage"
def from1toMatrix(vector,Nr,Nz):
    
    a=vector.copy()
    newMatrix=np.zeros((Nz,Nr))
    
    for i in range(0,Nr):
        for j in range(0,Nz):
            pl=i+j*Nz
            newMatrix[j,i]=a[pl]
    return newMatrix
