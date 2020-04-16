# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:57:22 2020

@author: koval
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.colors as colors
from matplotlib.cm import ScalarMappable as sm

def animate(maille,NT):
    fig1 = plt.figure()
    vmax=np.amax(maille)
    vmin=np.amin(maille)
    norm=colors.Normalize(vmin=vmin,vmax=vmin)
    ims = [(plt.pcolormesh(maille[:,:,0]),)]
    for i in np.arange(1, NT):
        ims.append((plt.pcolormesh(maille[:,:,i],vmin=vmin,vmax=vmax),))
        
    plt.gca().invert_yaxis()
    plt.colorbar(sm(norm=norm))
    im_ani = animation.ArtistAnimation(fig1, ims, interval=10, repeat_delay=1000,
                                   blit=True)
    
# To save this second animation with some metadata, use the following command:
    im_ani.save('im.mp4', metadata={'artist':'Les gars du projets'})
    plt.show()