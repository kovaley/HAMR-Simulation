# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:05:43 2020

@author: thomas
"""


import Terme_Source as TS
import numpy as np
import ploting as plt

P_las = 1e-3 #W
pC = 7800*432
Nr = 100 
Nz = 100
r_pos = 1e-9*np.arange(Nr) #m
z_pos = 1e-9*np.arange(Nz) #m
dt = 1e-10 #s
Nt = 150

source=np.zeros((Nz,Nr, Nt))
for t in range(0,Nt-1):
    source[:,:,t]=dt/pC*TS.SourceCreation(r_pos, z_pos, Nr, Nz, t*dt, P_las)


plt.animate(source,Nt)