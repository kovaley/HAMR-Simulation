#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:54:28 2020

@author: josephbattesti
"""
import matplotlib.pyplot as plt
import numpy as np

"Plot d'un frame"
def plotFrame(Maille,frame):
    plt.pcolor(Maille[:,:,frame])
    plt.colorbar()
    plt.show()

"Sauver chaque plot en .png pour ensuite render une animation avec ffmpeg"
def SaveFrames(Maille) :
    Nt=np.shape(Maille)[2]
    for frame_index in range(0, Nt):
            im=plt.imshow(
                        Maille[:,
                               :,
                               frame_index],)
            plt.colorbar(im)
            plt.savefig('frames/'+f"{frame_index:06d}_animation.png")
            plt.show()
            plt.close()

