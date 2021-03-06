# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:05:43 2020

@author: thomas
"""


import Terme_Source as TS
import numpy as np
import ploting as ploting
import matplotlib.pyplot as plt

P_las = 1e-3 #W
pC = 8900*432
Nr = 500 
Nz = 500
r_pos = 5e-9*np.arange(Nr) #m
z_pos = 5e-9*np.arange(Nz) #m
dt = 0.2e-9 #s
duree = 2e-9 #s
Nt = int(np.round(duree/dt))
print(Nt)

source=np.zeros((Nz,Nr, Nt))
for t in range(0,Nt-1):
    source[:,:,t]=dt/pC*TS.SourceCreation(r_pos, z_pos, Nr, Nz, t*dt, P_las)


im_ani = ploting.animate(source)

plt.title('Source pulsée en Kelvin')
plt.xlabel('rayon [nm]')
plt.ylabel('pronfondeur [nm]')

# im_ani.save('../../../source_sans_log.mp4', metadata={'artist':'Les gars du projets'})