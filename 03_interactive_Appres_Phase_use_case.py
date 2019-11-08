import numpy as np 
import matplotlib.pyplot as plt
from MT.MT import forwardMT

frequency = np.logspace(-4,4,100)

### Model 1
resistivity = np.array([100,200,20,1000,200])
thickness = np.array([100,100,100,100,100])

### Model 2
resistivity2 = np.array([100,200,30,1000,200])
thickness2 = np.array([100,100,100,100,100])

### Model 3
resistivity3 = np.array([100,200,40,1000,200])
thickness3 = np.array([100,100,100,100,100])

### Model 4
resistivity4 = np.array([100,200,70,1000,200])
thickness4 = np.array([100,100,100,100,100])

### Obs. Model 1
resistivity_obs = np.array([100,200,50,1000,200])
thickness_obs = np.array([100,100,100,100,100])

### forward model
appres = np.zeros([len(frequency),1])
phase = np.zeros([len(frequency),1])

appres2 = np.zeros([len(frequency),1])
phase2 = np.zeros([len(frequency),1])

appres3 = np.zeros([len(frequency),1])
phase3 = np.zeros([len(frequency),1])

appres4 = np.zeros([len(frequency),1])
phase4 = np.zeros([len(frequency),1])

appres_obs = np.zeros([len(frequency),1])
phase_obs = np.zeros([len(frequency),1])

print("hello")
for i in range(len(frequency)):
    appres[i], phase[i] = forwardMT(resistivity, thickness, frequency[i])
    
    appres2[i], phase2[i] = forwardMT(resistivity2, thickness2, frequency[i])
    
    appres3[i], phase3[i] = forwardMT(resistivity3, thickness3, frequency[i])
    
    appres4[i], phase4[i] = forwardMT(resistivity4, thickness4, frequency[i])
    
    appres_obs[i], phase_obs[i] = forwardMT(resistivity_obs, thickness_obs, frequency[i])
    

appres_all = [appres, appres2, appres3, appres4]

phase_all = [phase, phase2, phase3, phase4]


# plt.ion()
fig1 = plt.figure(num=1,figsize=(5,5))
# mng = plt.get_current_fig_manager()
# mng.Maximize(True)

plotAppres = fig1.add_subplot(2,2,1)
plotPhase =  fig1.add_subplot(2,2,3)

# Appres_curve, = plotAppres.loglog(frequency,[])
# Phase_curve, = plotPhase.loglog(frequency,[])

# Appres_curve, = plotAppres.loglog()
# Phase_curve, = plotPhase.loglog()

# print(len(appres_all))
# print(range(len(appres_all)))

plotAppres.loglog(frequency, appres_obs, '.r')
plotPhase.loglog(frequency, phase_obs, '.r')

plt.ion()
for i in range(len(appres_all)):
    if i == 0:
        Appres_curve, = plotAppres.loglog(frequency, appres_all[i])
        Phase_curve, = plotPhase.loglog(frequency, phase_all[i])

    else:
        Appres_curve.set_ydata(appres_all[i])
        Phase_curve.set_ydata(phase_all[i])
    print(i)
    fig1.canvas.draw()
    plt.pause(0.5)

    
    
plt.ioff()
plt.show()

    
# for appres_plot, phase_plot in zip(appres_all, phase_all):
#     i += 0.01
#     print(appres_plot)
#     print(phase_plot)
#     # Appres_curve.set_ydata(appres_plot)
#     # Phase_curve.set_ydata(phase_plot)

#     # plt.clf()
#     # fig1.canvas.draw()
#     # plt.pause(0.5)
# print(phase)
# plt.ioff()
# plt.show()


    
          

   

    






