# -*- coding: utf-8 -*-

import numpy as np


def SourceCreation(dr, dz, Nr, Nz, t, P_las):
    k = 2*np.pi/(780e-9) #m^-1
    sigma = 4.961e5 #(ohm m)^-1
    a = 10e-9 #m
    c = 299792458 #m/s
    omega = c/k #rad/s
    eps_0 = 8.85418782e-12 #F/m
    n_air = 1
    tau_0 = 10e-9 #ns
    t_0 = 5*tau_0
    Im_n = 4.73 
    
    r =  dr*np.arange(Nr)
    z =  dz*np.arange(Nz)   
    
    Source = 4*sigma*a**4*P_las/(c*np.pi*eps_0*n_air * (r**2+z**2)**5) * ((3*r**2 - 1)**2 \
    + (3*r*z)**2)*np.cos(k*z-omega*t)**2 * np.sin(omega*(t-t_0))**2*np.exp(-(t-t_0)**2/tau_0**2) \
    *np.exp(-Im_n*np.sqrt(2)*k*(r+z))
    
    
    return Source