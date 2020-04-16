# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:05:43 2020

@author: thomas
"""


import Terme_Source as TS
import numpy as np
import matplotlib.pyplot as plt

P_las = 1e-3 #W
pC = 7800*432
Nr = 100 
Nz = 100
r_pos = 1e-9*np.arange(Nr) #m
z_pos = 1e-9*np.arange(Nz) #m
dt = 1e-10 #s
Nt = 50

source=np.zeros((Nz,Nr))
source[:,:]=dt/pc*TS.SourceCreation(r_pos, z_pos, Nr, Nz, Nt*dt, P_las)


plt.matshow(source)
plt.figure(2)
y = source[1,:]
plt.plot(r_pos,y)

