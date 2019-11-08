import numpy as np 
import matplotlib.pyplot as plt
from MT.MT import forwardMT





        
        

        
        


resistivity = np.array([100,200,50,1000,200])

thickness = np.array([100,100,100,100,100])
frequency = np.logspace(-4,4,100)
# print(frequency)
# print(thickness)
# print(resistivity)
appres = np.zeros([len(frequency),1])
phase = np.zeros([len(frequency),1])
for i in range(len(frequency)):
    # print(i)
    appres[i],phase[i] = forwardMT(resistivity, thickness, frequency[i])
    
    
plt.ion()
fig1 = plt.figure(num=1,figsize=(5,5))

plotAppres = fig1.add_subplot(2,2,1)
plotPhase =  fig1.add_subplot(2,2,3)

Appres_curve, = plotAppres.loglog(frequency,appres)
Phase_curve, = plotPhase.loglog(frequency,phase)
# print(Appres_curve)


i = 0
for increment in np.logspace(0,2,5):
    i += 0.01
    print(i)
    Appres_curve.set_ydata(appres + increment)
    Phase_curve.set_ydata(phase + i)

    # plt.clf()
    fig1.canvas.draw()
    plt.pause(0.5)
print(phase)
plt.ioff()
plt.show()


    
          

   

    






