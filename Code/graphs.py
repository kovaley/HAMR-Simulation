# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:10:09 2020

@author: koval
"""

import euler_Implicite as euImp
import numpy as np
import ploting as plt
import time
import Terme_Source as TS
import matplotlib.pyplot as plot
import simulate as s



"Dimensions"
Lr=300e-9
Lz=300e-9
duration=50e-9
"Nombre de celulles"
Nt=100;
Nr=10;
Nz=10;

dr=Lr/Nr;
dz=Lz/Nz;
dt=duration/Nt

P_las=10e-3


for fact in [1, 1/2, 1/4, 1/8] :
    Maille=s.simulate(P_las,Nz*fact,Nr*fact,Nt,Lr,Lz,duration)



d_ar=[]
tinv_ar=[]
mem_ar=np.zeros(0)
Tm_ar=[]





Tcurie=310
rayonbit=dr*np.sum(Maille[:,10,:]>Tcurie,axis=0)
plot.plot(dt*np.arange(0,Nt),rayonbit)


np.append(mem_ar, 8*(Nr*Nz*Nt)^2)





