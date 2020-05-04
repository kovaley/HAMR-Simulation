# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:02:34 2020

@author: koval
"""

import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation



temps_exec=np.log(np.array(t_exec))
x1=np.log(np.array(x))
m,b = np.polyfit(x1, temps_exec, 1)
print(m)
print(b)

memory_usage1=np.log(np.array(memory_usage))
m,b = np.polyfit(x1, memory_usage1, 1)
print(m)
print(b)
