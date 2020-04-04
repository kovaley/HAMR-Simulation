#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"Vecteur des temperature (step1) to maillage"
def VectorToMatrix(vector,Nr,Nz):
    
    a=vector.copy()
    newMatrix=np.zeros((Nz,Nr))
    
    for i in range(0,Nr):
        for j in range(0,Nz):
            pl=i+j*Nr
            newMatrix[j,i]=a[pl]
    return newMatrix
