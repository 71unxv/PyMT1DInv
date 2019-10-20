import numpy as np 
import matplotlib.pyplot as plt


def forwardMT(resistivity, thickness, frequency):
    mu = 4*np.pi *1E-7
    w = 2* np.pi*frequency
    nn = len(resistivity)
    impedance = np.zeros([nn,1], dtype=complex)
    
    Zn = np.sqrt(1j *w*mu*resistivity[-1])
    
    impedance[-1] = Zn

    for i in np.arange(nn-2,-1,-1):
        dj = np.sqrt(1j*(w*mu*(1/resistivity[i])))
        wj = dj * resistivity[i]
        
        ej = np.exp(-2*thickness[i]*dj)
        belowImpedance = impedance[i+1]
        
        rj = (wj - belowImpedance)/(wj + belowImpedance)
        re = rj*ej
        zj = wj * ((1-re)/(1+re))

        impedance[i] = zj
        
    z = impedance[0]
    absZ = np.abs(z)
    
    apparentResistivity = (absZ * absZ)/(mu * w)
    phase = np.arctan2(z.imag, z.real)
    
    return apparentResistivity, phase
        

        
        


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
    
    
    
fig1 = plt.figure(num=1,figsize=(5,5))
plotAppres = fig1.add_subplot(2,2,1)
plotPhase =  fig1.add_subplot(2,2,3)
plotAppres.loglog(frequency,appres)
plotPhase.loglog(frequency,phase)


plt.show()

    
          

   

    






