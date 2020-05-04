# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:02:34 2020

@author: koval
"""

import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation



erreur=np.log(list(np.array(temp200nm[1:]) - np.array(temp200nm[0:-1])))
x1=np.log(np.array(x[1:]))
m,b = np.polyfit(x1, erreur, 1)
print(m)
print(b)
