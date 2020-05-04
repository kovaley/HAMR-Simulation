#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import euler_Implicite as euImp
import crankNicolson as CR
import numpy as np
import ploting as plt
import time
import Terme_Source as TS
import nu_grid as nu_grid
from scipy.sparse import linalg as lina
from scipy.sparse import lil_matrix as lil


"Parametres physiques"
rho=8900  #kg.m-3
cSpe=423  #J.Kg-1.K-1
pC=rho*cSpe
k_para=84 #W.m-1.K-1
k_perp=84 #W.m-1.K-1
h=10 #convection
alpha_para=k_para/(pC)
alpha_perp=k_perp/(pC)
Tp=0
Tini=0
P_las=1e-3

"Pas de temps"
deltat=1e-9

"Dimensions"
<<<<<<< Updated upstream
=======
Lr=500e-9   #m
Lz=500e-9   #m
duration=20e-9 #s

"Pas"
deltat=0.15e-9;
deltar=5e-9;
deltaz=5e-9;

"Nombre de celulles"
Nr=int(np.round(Lr/deltar))
Nz=int(np.round(Lz/deltaz))
Nt=int(np.round(duration/deltat))

sampling_depth=int(20e-9/Lz*Nz) #nm


P_las=1e-3   #W  
resultats=[]
rayonbit=[]
t_exec = []
t= []
x = []
memory_usage = []
rayon_max = []

"active le tracage des profils de rayon de bits"
rayonbit_enable=0
#0=disabled
#1=enabled
"choix de la boucle à exécuter"
boucle=3;
#0=pas de temps
#1=spatiale
#2=puissance laser
#2=test de la source

test_enable = 1 


"boucle pas de temps"
if boucle==0 :
    for fact in [1, 1/2, 1/4, 1/8] :
        simulation, execution_time, memory_use=simulate.simulate(P_las,deltaz,deltar,deltat*fact,Lr,Lz,duration)
        rayonbit.append(deltar*10**9*np.sum(simulation[sampling_depth,:,:]>Tcurie,axis=0))#rayon du bit en fonction du temps
        t.append(fact*deltat*np.arange(0,int(np.round(duration/(deltat*fact))))*10**9)#abscisse rayon du bit
        resultats.append(simulation)                #simulation   
        t_exec.append(execution_time)               #temps d'exécution
        x.append(deltat*fact*10**9)              #Pas de temps
        memory_usage.append(memory_use)             #utilisation de la mémoire
        rayon_max.append(10**9*np.amax(deltar*np.sum(simulation[sampling_depth,:,:]>Tcurie,axis=0))) #rayon maximal

    "Étiquettes des graphiques"   
    xlabel1='pas de temps (ns)'
    plottitle1='temps d''exécution en fonction du pas de temps'
    plottitle2='mémoire utilisée en fonction du pas de temps'
    plottitle3='rayon maximum en fonction du pas de temps'        
    plottitle4 = 'erreur sur le rayon maximal en fonction du pas de temps'    
    
    
    
    
"Boucle pas spatiaux"
if boucle==1 :
    for fact in [1, 1/2, 1/4, 1/8] :
        simulation, execution_time, memory_use=simulate.simulate(P_las,deltaz*fact,deltar*fact,deltat,Lr,Lz,duration)
        rayonbit.append(deltar*10**9*np.sum(simulation[int(sampling_depth/fact),:,:]>Tcurie,axis=0))#rayon du bit en fonction du temps  
        t.append(deltat*np.arange(0,Nt)*10**9)      #abscisse rayon du bit        
        resultats.append(simulation)                #simulation   
        t_exec.append(execution_time)               #temps d'exécution
        x.append(deltar*fact*10**9)                 #Pas spatial
        memory_usage.append(memory_use)             #utilisation de la mémoire
        rayon_max.append(10**9*np.amax(deltar*np.sum(simulation[int(sampling_depth/fact),:,:]>Tcurie,axis=0))) #rayon maximal


    "Étiquettes des graphiques"           
    xlabel1='pas spatial (nm)'
    plottitle1='temps d''exécution en fonction du pas spatial'
    plottitle2='mémoire utilisée en fonction du pas spatial'  
    plottitle3='rayon maximum en fonction du pas spatial'
    plottitle4 = 'erreur sur le rayon maximal en fonction du pas spatial'
    
    
    
    

"Boucle puissance du laser"
if boucle==2 :
    for fact in [1, 1e2, 1e3, 1e4]:
        simulation, execution_time, memory_use=simulate.simulate(P_las*fact,deltaz,deltar,deltat,Lr,Lz,duration)
        rayonbit.append(deltar*10**9*np.sum(simulation[sampling_depth,:,:]>Tcurie,axis=0))#rayon du bit en fonction du temps
        t.append(deltat*np.arange(0,Nt)*10**9)      #abscisse rayon du bit  
        resultats.append(simulation)                #simulation   
        t_exec.append(execution_time)               #temps d'exécution
        x.append(P_las*fact)                        #Pas de temps
        memory_usage.append(memory_use)             #utilisation de la mémoire
        rayon_max.append(10**9*np.amax(deltar*np.sum(simulation[sampling_depth,:,:]>Tcurie,axis=0))) #rayon maximal
    
    "Étiquettes des graphiques"    
    xlabel1='Puissance du laser (mW)'
    plottitle1='Temps d''exécution en fonction de la puissance du laser'
    plottitle2='Mémoire utilisée en fonction de la puissance du laser'
    plottitle3='rayon maximum en fonction de la puissance du laser'
    plottitle4 = 'erreur sur le rayon maximal en fonction de la puissance du laser'



"Boucle de test de la source"
if boucle==3 :
    simulation, execution_time, memory_use=simulate.simulate(P_las,deltaz,deltar,deltat,Lr,Lz,duration)
    rayonbit.append(deltar*10**9*np.sum(simulation[sampling_depth,:,:]>Tcurie,axis=0))#rayon du bit en fonction du temps
    t.append(deltat*np.arange(0,Nt)*10**9)      #abscisse rayon du bit 
    resultats.append(simulation)                #simulation   
    im_ani1 = plt.animate(resultats[0])
        
    "tracage du rayon selon t"
    # figure2=plot.figure()
    # plot.plot(t[0],rayonbit[0])
    # plot.xlabel('temps (ns)')
    # plot.ylabel('rayon du bit (nm)')
    # plot.title('rayon selon t')
        
        
if test_enable == 0:       
    "Plotting et animation"

    "Animation du résultat dernier"   
    im_ani1 = plt.animate(resultats[0])
    
    
    
    "tracage du temps d''exécution"
    figure1=plot.figure()
    plot.loglog(x,t_exec,'o')
    plot.loglog(x,t_exec,'-')
    plot.loglog(x,t_exec)
    plot.xlabel(xlabel1)
    plot.ylabel('temps d''exéxution (s)')
    plot.title(plottitle1)
    
    
    "tracage de l'utilation de la mémoire"
    figure2=plot.figure()
    plot.loglog(x,memory_usage,'o')
    plot.loglog(x,memory_usage,'-')
    plot.xlabel(xlabel1)
    plot.ylabel('utilisation de la mémoire (Mo)')
    plot.title(plottitle2)
    
    
    "tracage du rayon maximum"
    figure3=plot.figure()
    plot.plot(x,rayon_max)
    plot.xlabel(xlabel1)
    plot.ylabel('rayon maximum du bit (nm)')
    plot.title(plottitle3)
    
    "Tracage de l'erreur"
    figure4=plot.figure()
    plot.plot(x[1:],list(np.array(rayon_max[1:]) - np.array(rayon_max[0:-1])))#not the fastest way, but it's working
    plot.xlabel(xlabel1)
    plot.ylabel('erreur sur le rayon (nm)')
    plot.title(plottitle4)
    
    "Tracage des profils de rayon de bit"
    if rayonbit_enable==1:
        figure5, axs = plot.subplots(2,2)
        axs[0, 0].plot(t[0],rayonbit[0])
        axs[0, 0].set_title('dt1')
        axs[0, 1].plot(t[1],rayonbit[1])
        axs[0, 1].set_title('dt2')
        axs[1, 0].plot(t[2],rayonbit[2])
        axs[1, 0].set_title('dt3')
        axs[1, 1].plot(t[3],rayonbit[3])
        axs[1, 1].set_title('dt4')
        for ax in axs.flat:
            ax.set(xlabel='temps', ylabel='rayon du bit')     






>>>>>>> Stashed changes

Nt=100;
Nr=100;
Nz=100;


duration=Nt*deltat;#s
"Maillage"
a=10
k=100e-9 #Domaine de simulation
# r_pos, z_pos, deltar,deltaz=nu_grid.get_grid(Nr,Nz,a,k);
r_pos = k/Nr*np.arange(Nr+1)
z_pos = k/Nz*np.arange(Nz+1)
deltar = k/Nr*np.ones(Nr)
deltaz = k/Nz*np.ones(Nz)

# deltat=1/(4*(alpha_para/(deltar)**2+alpha_perp/(deltaz)**2)); #s


# "Condition de stabilité"
# crit=deltat*(alpha_para/(deltar)**2+alpha_perp/(deltaz)**2)
# if crit>0.5:
#     print("big, ça sera pas stable")
 
# print(Nr,Nz,Nt)

N=Nr*Nz;


"Matrices de coefficients d'un cranknicolson"
A,B,C=CR.buildMatrix1(Nr,Nz, 
                         alpha_para, 
                         alpha_perp, 
                         deltar, deltat, deltaz,
                         pC,h,Tp)

print("Matrix Done")

"Temperature initiale."
Maille = np.zeros((Nz,Nr,Nt));
Maille[:,:,0]=Tini

source=np.zeros((Nz,Nr,Nt))
for t in range(0,Nt-1)   :
    for i in range(0,Nr-1) :
        for j in range(0,Nz-1) :
            if (j>50) :
                source[j,i,t]=20
    
source1=source[:,:,0]
source1=source1.flatten().reshape(-1,1)
mailloche=Maille[:,:,0].flatten().reshape(-1, 1)
d=B.dot(Maille[:,:,0].flatten().reshape(-1, 1))+C+source1.flatten().reshape(-1,1);
T=np.linalg.solve(A,d)
soletgoblet=T.reshape(Maille[:,:,0].shape)    
print("Initial conditions Done")

#startime = time.time()
#"Iteration temporelle / Calcul de la solution"
#for t in range(0,Nt-1)    :
#    # source[:,:,t]=deltat*TS.SourceCreation(r_pos, z_pos, Nr,
#                                            # Nz, t*deltat, P_las)/pC
#    
#    Maille[:,:,t+1]=CR.solve(Maille[:,:,t],A,B,C,source[:,:,t])
#    
#    
#execution_time = time.time()-startime 
#print("Computation of solution done in {:.2f} seconds".format(execution_time))
#    
#"Plotting et animation"
#
#plt.animate(Maille,Nt)
## plt.animate(source,Nt)
#

print("Plotting Done")         


          
            
            
            