import numpy as np

class Model:
    
    def __init__(self ,resistivity, thickness):
        self.thickness = thickness
        self.resistivity = resistivity
    
    
class Data:
    def __init__(self, frequency, appres=0, phase=0,info = "pyMT1D"):
        self.frequency = frequency
        self.appres = appres
        self.phase = phase
        self.info = info
        

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


def jacobianMT(frequency, resistivity, thickness, perturb_value=0.01):
    if len(resistivity.shape) == 1:
        resistivity = resistivity[:,None]

    resistivity_temp = resistivity.copy()
    appres = np.zeros(len(frequency))
    phase = np.zeros(len(frequency))

    for freq in range(len(frequency)):
        appres[freq] ,phase[freq] = forwardMT(np.exp(resistivity), thickness, frequency[freq])

    J_appres = np.zeros((len(frequency), len(resistivity)))
    J_phase = np.zeros((len(frequency), len(resistivity)))

    for i in range(len(resistivity)):

        dm = resistivity[i] * perturb_value

        resistivity_temp[i] = resistivity[i] + dm
        for freq in range(len(frequency)):

            appres_temp ,phase_temp = forwardMT(np.exp(resistivity_temp), thickness, frequency[freq])

            J_appres[freq, i] = (np.log(appres[freq]) - np.log(appres_temp))/(dm)
            J_phase[freq, i] = (np.log(phase[freq]) - np.log(phase_temp))/(dm)
    return J_appres, J_phase