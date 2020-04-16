# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:02:15 2020

@author: thomas
"""

# Fonction qui calcule un maillage non-uniforme de type exponnentiel. 
# On remarque que le Nième terme est égal à 1.
# Le paramètre k représente la dimension du Nième terme
# a est le taux de streching de la grille. Plus a est grand et plus la grille est étirée.
import numpy as np
# import matplotlib.pyplot as plt


def get_grid( Nr, Nz, a, k):
    
    r = np.arange(Nr+1)
    z = np.arange(Nz+1)
    r_pos = k*(np.exp(a*r/Nr)-1)/(np.exp(a)-1)
    z_pos = k*(np.exp(a*z/Nz)-1)/(np.exp(a)-1)
    dr = r_pos[1:]-r_pos[0:-1]
    dz = z_pos[1:]-z_pos[0:-1]
    
    return r_pos, z_pos, dr, dz

# Nr = 100
# Nz = Nr
# a = 5
# k = 1 #m


# r_pos, z_pos, dr, dz = get_grid(Nr, Nz, a, k)
# plt.plot(np.arange(Nr),dr)
# plt.figure(2)
# plt.plot(np.arange(Nr+1),r_pos)
