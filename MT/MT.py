import numpy as np

class Model:
    
    def __init__(self,thickness,resistivity):
        self.thickness = thickness
        self.resistivity = resistivity
    
    
class Data:
    def __init__(self, frequency,resistivity=0, phase=0,info = "pyMT1D"):
        self.frequency = frequency
        self.resistivity = resistivity
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

def jacobianMT(resistivity, frequency, thickness=0):
    if thickness==0:
        
        
        
        return J
    else:
        return J
        
