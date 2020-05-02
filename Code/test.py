# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:02:34 2020

@author: koval
"""

import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

figure4, axs = plot.subplots(2,2)
axs[0, 0].plot(t[1],rayonbit[1])
axs[0, 0].set_title('Axis [0,0]')
axs[0, 1].plot(t[1],rayonbit[1])
axs[0, 1].set_title('Axis [0,1]')
axs[1, 0].plot(t[2],rayonbit[2])
axs[1, 0].set_title('Axis [1,0]')
axs[1, 1].plot(t[3],rayonbit[3])
axs[1, 1].set_title('Axis [1,1]')
for ax in axs.flat:
    ax.set(xlabel='temps', ylabel='rayon du bit')          