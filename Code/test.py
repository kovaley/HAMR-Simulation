# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:02:34 2020

@author: koval
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation




"Tracage de l'erreur"
figure4=plot.figure()
plot.loglog(x[2:],list(np.array(temp200nm[2:]) - np.array(temp200nm[1:-1])),'o')#not the fastest way, but it's working
plot.loglog(x[2:],list(np.array(temp200nm[2:]) - np.array(temp200nm[1:-1])),'-')#not the fastest way, but it's working
plot.xlabel(xlabel1)
plot.ylabel('erreur sur la température')
erreur=np.log(list(np.array(temp200nm[2:]) - np.array(temp200nm[1:-1])))
x1=np.log(np.array(x[2:]))
m,b = np.polyfit(x1, erreur, 1)
p = np.poly1d(np.polyfit(x1, erreur, 1))
t = np.linspace(1, 1, 200)
plot(t, p(t), '-')
print(m)
print(b)