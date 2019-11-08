
from MT.MT import forwardMT, jacobianMT
import numpy as np 
import matplotlib.pyplot as plt

frequency = np.logspace(-4,4,100)

### Model 1
resistivity = np.log(np.array([100,100,100,100,100]))
thickness = np.array([100,100,100,100,100])
perturb_value = 0.05
# perturb_value = 1 + perturb_value
resistivity = resistivity[:,None]


resistivity_temp = resistivity.copy()
appres = np.zeros(len(frequency))
phase = np.zeros(len(frequency))
# print(appres.shape)
for freq in range(len(frequency)):
    appres[freq] ,phase[freq] = forwardMT(np.exp(resistivity), thickness, frequency[freq])


#      (f(m) - f(m+dm))/dm
# print(type(len(resistivity)))
J = np.zeros((len(frequency), len(resistivity)))
J[:] = np.nan


# print(J)
print(J.shape)
# print(type(J))
# print(type(J[0,0]))
# print(appres)
for i in range(len(resistivity)):
    print(i)
    dm = resistivity[i] * perturb_value

    resistivity_temp[i] = resistivity[i] + dm
    for freq in range(len(frequency)):
        print(freq)
        appres_temp ,phase_temp = forwardMT(np.exp(resistivity_temp), thickness, frequency[freq])
        # print(appres_temp)
        
        result = (np.log(appres[freq]) - np.log(appres_temp))/(dm)
        J[freq, i] = result
        # print(result)
        # print(J)
print(J)


#     resistivity_temp = resistivity.copy()
    
    



# a = np.random.rand(5,2)
# # a = a[:, None]

# # b = a[:,0:1]
# print(a)
# for i in range(len(a)):
#     print(a[i][1])
#     print("-")
debug = []






