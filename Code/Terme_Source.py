# -*- coding: utf-8 -*-

import numpy as np


def SourceCreation(r_pos, z_pos, Nr, Nz, t, P_las):
    k = 2*np.pi/(780e-9) #m^-1
    sigma = 4.961e5 #(ohm m)^-1
    a = 10e-9 #m
    c = 299792458 #m/s
    omega = c*k #rad/s
    eps_0 = 8.85418782e-12 #F/m
    n_air = 1
    tau_fwhm = 3e-9 #s
    tau_0 = tau_fwhm/(2*np.sqrt(np.log(2))) #s
    t_0 = 5*tau_0 #s
    Im_n = 4.73 
    Source=np.zeros((Nz,Nr))
    dr = r_pos[2]-r_pos[1]
    dz = z_pos[2]-z_pos[1]
    
    "Parametres physiques"
    rho=8900  #kg.m-3
    cSpe=423  #J.Kg-1.K-1
    pC=rho*cSpe
    k_z=84 #W.m-1.K-1
    k_r=84 #W.m-1.K-1
    alpha_z=k_z/(pC)
    alpha_r=k_r/(pC)
    
    
    for i in range(0,Nz):
        for j in range(0,Nr):

                r =  r_pos[j]+10e-9 #m
                z =  z_pos[i]+10e-9 #m
                
                if (0<i<Nz-1) and (0<j<Nr-1):
                    Source[i,j] = 1e2*4*sigma*a**4*P_las/(c*np.pi*eps_0*n_air*(r**2+z**2)**3) * ((3*r**2/(r**2+z**2)-1)**2 \
                            + (z*r/(r**2+z**2))**2)*np.exp(-(t-t_0)**2/tau_0**2) \
                            *np.exp(-Im_n*np.sqrt(2)*k*(r+z))*1/2*dr**2*dz**2/(alpha_r*alpha_z)
                    # Source[i,j] = 1e23*P_las*np.exp(-((r-200e-9)/10e-9)**2)*np.exp(-((z-200e-9)/10e-9)**2)*np.exp(-(t-t_0)**2/tau_0**2)


    
    return Source

#*np.cos(k*z-omega*t)**2