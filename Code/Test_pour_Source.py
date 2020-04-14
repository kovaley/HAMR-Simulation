# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:05:43 2020

@author: thomas
"""


import Terme_Source as TS
import numpy as np
import matplotlib.pyplot as plt

P_las = 1e-3 #W

dr = 1e-9 #m
dz = 1e-9 #m
Nr = 300 
Nz = 300
dt = 1e-9 #s
Nt = 10

source=np.zeros((Nz,Nr))
source[:,:]=TS.SourceCreation(dr, dz, Nr, Nz, Nt*dt, P_las)


plt.matshow(source)
plt.figure(2)
x = np.arange(0,dz*Nz,dz)
y = source[:,1]
plt.plot(x,y)

