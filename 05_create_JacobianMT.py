
from MT.MT import forwardMT, jacobianMT
import numpy as np 
import matplotlib.pyplot as plt

frequency = np.logspace(-4,4,100)
resistivity = np.log(np.array([100,100,100,100,100]))
thickness = np.array([100,100,100,100,100])

perturb_value = 0.05

# if resistivity.shape
print(len(resistivity.shape))
resistivity = resistivity[:,None]
resistivity = resistivity.ravel()
print(resistivity.shape)
# print(len(resistivity.shape))
print(resistivity)


# def jacobianMT(frequency, resistivity, thickness, perturb_value=0.01):

#     resistivity = resistivity[:,None]

#     resistivity_temp = resistivity.copy()
#     appres = np.zeros(len(frequency))
#     phase = np.zeros(len(frequency))

#     for freq in range(len(frequency)):
#         appres[freq] ,phase[freq] = forwardMT(np.exp(resistivity), thickness, frequency[freq])

#     J_appres = np.zeros((len(frequency), len(resistivity)))
#     J_phase = np.zeros((len(frequency), len(resistivity)))

#     for i in range(len(resistivity)):

#         dm = resistivity[i] * perturb_value

#         resistivity_temp[i] = resistivity[i] + dm
#         for freq in range(len(frequency)):

#             appres_temp ,phase_temp = forwardMT(np.exp(resistivity_temp), thickness, frequency[freq])

#             J_appres[freq, i] = (np.log(appres[freq]) - np.log(appres_temp))/(dm)
#             J_phase[freq, i] = (np.log(phase[freq]) - np.log(phase_temp))/(dm)
#     return J_appres, J_phase






