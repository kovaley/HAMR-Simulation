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
    ims = []
    for i in np.arange(0, NT):
        ims.append((plt.pcolor(maille[:,:,i]),))
    plt.gca().invert_yaxis()
    im_ani = animation.ArtistAnimation(fig1, ims, interval=50, repeat_delay=3000,
                                   blit=True)
    plt.colorbar()
# To save this second animation with some metadata, use the following command:
    im_ani.save('im.mp4', metadata={'artist':'Les gars du projets'})
    plt.show()