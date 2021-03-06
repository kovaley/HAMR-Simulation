#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:54:28 2020

@author: josephbattesti
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from matplotlib.cm import ScalarMappable as sm

"Plot d'un frame"
def plotFrame(Maille,frame):
    plt.pcolor(Maille[:,:,frame])
    plt.colorbar()
    plt.show()

"Sauver chaque plot en .png pour ensuite render une animation avec ffmpeg"
def SaveFrames(Maille) :
    Nt=np.shape(Maille)[2]
    norm=colors.Normalize(vmin=np.min(Maille),vmax=np.max(Maille))
    cmap='PuBu_r'
    for frame_index in range(0, Nt):
            im=plt.imshow(
                        Maille[:,
                               :,
                               frame_index],cmap=cmap,norm=norm)
            plt.colorbar(sm(norm=norm,cmap=cmap))
            
            plt.savefig('frames/'+f"{frame_index:06d}_animation.png")
            plt.show()
            plt.close()

