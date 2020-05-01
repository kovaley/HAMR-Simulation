#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import euler_Implicite as euImp
import numpy as np
import ploting as plt
import time
import Terme_Source as TS
import nu_grid as nu_grid
import simulate as simulate
import matplotlib.pyplot as plot
#just want to hear when execution is done
import winsound
"constants"
Tcurie=1394 #K
sampling_depth=9 #cellules

"Dimensions"
Lr=500e-9
Lz=500e-9
duration=1e-9

"Pas"
deltat=0.2e-9;
deltar=1e-9;
deltaz=1e-9;

"Nombre de celulles"
Nr=int(np.round(Lr/deltar))
Nz=int(np.round(Lz/deltaz))
Nt=int(np.round(duration/deltat))


P_las=1**np.arange(1)*1e-3   #W  
resultats=[]
rayonbit=[]
t_exec = []
pasdetemps = []
memory_usage = []


"choix de la boucle à exécuter"
boucle=0;
#0=pas de temps
#1=spatiale
#2=puissance laser
#2=test de la source



"boucle pas de temps"
if boucle==0 :
    for fact in [1, 1/2, 1/4, 1/8] :
        simulation, execution_time, memory_use=simulate.simulate(P_las[0],deltaz,deltar,deltat*fact,Lr,Lz,duration)
        resultats.append(simulation)                #simulation   
        t_exec.append(execution_time)               #temps d'exécution
        pasdetemps.append(deltat*fact)              #Pas de temps
        memory_usage.append(memory_use)             #utilisation de la mémoire
        
        
        
    "Animation du résultat au pas de temps minimum"   
    im_ani1 = plt.animate(resultats[3])


    
    "tracage du temps d''exécution en fonction du pas de temps"
    figure1=plot.figure()
    plot.plot(pasdetemps,t_exec)
    plot.xlabel('pas de temps (ns)')
    plot.ylabel('temps d''exéxution (s)')
    plot.title('temps d''exécution en fonction du pas de temps')
    
    
    "tracage du temps d''exécution en fonction du pas de temps"
    figure2=plot.figure()
    plot.plot(pasdetemps,memory_usage)
    plot.xlabel('pas de temps (ns)')
    plot.ylabel('utilisation de la mémoire (octets)')
    plot.title('Utilisation de la mémoire en fonction du pas de temps')
    
    
    
"Boucle pas spatiaux"
if boucle==1 :
    for fact in [1, 1/2, 1/4, 1/8] :
        
        resultats.append(simulate.simulate(P_las[0],deltaz*fact,deltar*fact,deltat,Lr,Lz,duration))   







"Boucle puissance du laser"
if boucle==2 :
    for n in range(0,len(P_las)):
        resultats.append(simulate.simulate(P_las[n],deltaz,deltar,deltat,Lr,Lz,duration))
        rayonbit.append(deltar*np.sum(resultats[n][sampling_depth,:,:]>Tcurie,axis=0))
        








"Boucle de test de la source"
if boucle==3 :
    for n in range(0,len(P_las)):
        resultats.append(simulate.simulate(P_las[n],deltaz,deltar,deltat,Lr,Lz,duration))
        rayonbit.append(deltar*np.sum(resultats[n][sampling_depth,:,:]>Tcurie,axis=0))
        
        
        
        
        
        
"Plotting et animation"

# plot.plot(deltat*np.arange(0,Nt)*10**9,rayonbit[0]*10**9)
# plot.xlabel('temps [ns]')
# plot.ylabel('rayon d''un bit [nm]')
# plot.title('Rayon d''un bit selon le temps d''une impulsion')

#im_ani1 = plt.animate(resultats[0])
#im_ani2 = plt.animate(resultats[1])
# plt.animate(source,Nt)


print("Plotting Done")   

winsound.Beep(500,2000)
          
            
            
            