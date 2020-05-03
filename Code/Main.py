#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import ploting as plt
import nu_grid as nu_grid
import simulate as simulate
import matplotlib.pyplot as plot
#just want to hear when execution is done
import winsound
"constants"
#Tcurie=1394 #K
Tcurie=400 #K


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

sampling_depth=int(200e-9/Lz*Nz) #nm


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
        rayon_max.append(10**9*np.amax(deltar*np.sum(simulation[sampling_depth/fact,:,:]>Tcurie,axis=0))) #rayon maximal


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
    for n in range(0,len(P_las)):
        simulation, execution_time, memory_use=simulate.simulate(P_las,deltaz,deltar,deltat,Lr,Lz,duration)
        # rayonbit.append(deltar*10**9*np.sum(simulation[sampling_depth,:,:]>Tcurie,axis=0))#rayon du bit en fonction du temps
        # t.append(deltat*np.arange(0,Nt)*10**9)      #abscisse rayon du bit 
        resultats.append(simulation)                #simulation   
        im_ani1 = plt.animate(resultats[0])
        
        
        
        
if test_enable == 1:       
    "Plotting et animation"

    "Animation du résultat dernier"   
    im_ani1 = plt.animate(resultats[0])
    
    
    
    "tracage du temps d''exécution"
    figure1=plot.figure()
    plot.plot(x,t_exec)
    plot.xlabel(xlabel1)
    plot.ylabel('temps d''exéxution (s)')
    plot.title(plottitle1)
    
    
    "tracage de l'utilation de la mémoire"
    figure2=plot.figure()
    plot.plot(x,memory_usage)
    plot.xlabel(xlabel1)
    plot.ylabel('utilisation de la mémoire (octets)')
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







# plot.plot(deltat*np.arange(0,Nt)*10**9,rayonbit[0]*10**9)
# plot.xlabel('temps [ns]')
# plot.ylabel('rayon d''un bit [nm]')
# plot.title('Rayon d''un bit selon le temps d''une impulsion')

#im_ani1 = plt.animate(resultats[0])
#im_ani2 = plt.animate(resultats[1])
# plt.animate(source,Nt)


print("Plotting Done")   

winsound.Beep(500,2000)
          
            
            
            