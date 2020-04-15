# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:57:22 2020

@author: koval
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def animate(maille,NT):
    fig1 = plt.figure()
    ims = [(plt.pcolormesh(maille[:,:,0]),)]
    plt.colorbar()
    for i in np.arange(1, NT):
        ims.append((plt.pcolormesh(maille[:,:,i],vmin=np.amin(maille[:,:,1]),vmax=np.amax(maille[:,:,1])),))
        
    plt.gca().invert_yaxis()
    
    im_ani = animation.ArtistAnimation(fig1, ims, interval=10, repeat_delay=1000,
                                   blit=True)
    
# To save this second animation with some metadata, use the following command:
    im_ani.save('im.mp4', metadata={'artist':'Les gars du projets'})
    plt.show()