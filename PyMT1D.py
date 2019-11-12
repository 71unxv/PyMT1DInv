import numpy as np
import matplotlib.pyplot as plt

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
        
class Visualize:
        
    def __init__(self, fig=plt.figure()):
        self.fig = fig
        gs = fig.add_gridspec(2, 2)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        
        self.figAppres = self.fig.add_subplot(gs[0,0])
        self.figPhase = self.fig.add_subplot(gs[1,0])
        self.figResistivity = self.fig.add_subplot(gs[0:,1])
        plt.suptitle("JI-PyMT1DInv a Magnetotelluric Inversion ver 0.1")
    def plot_Data_obs(self,Data_obs):
        self.figAppres.loglog(Data_obs.frequency, Data_obs.appres, '.r')
        self.figAppres.grid(b=True, which='minor', color='gray', linestyle='-', linewidth = 0.1)
        self.figPhase.loglog(Data_obs.frequency, Data_obs.phase, '.r')
        self.figPhase.grid(b=True, which='minor', color='gray', linestyle='-', linewidth = 0.1)
    
    def plot_Model_true(self, Model_true):
        # if Model_true != 0:
        self.figResistivity.step(Model_true.resistivity, -np.cumsum(Model_true.thickness), '--k')

    def plot_Inv(self, Data_pred, Model_pred, iter=1):
        if iter==1:
            self.Appres_curve, = self.figAppres.loglog(Data_pred.frequency, Data_pred.appres)
            self.Phase_curve, = self.figPhase.loglog(Data_pred.frequency, Data_pred.phase)
            self.Resistivity_plot, = self.figResistivity.step(Model_pred.resistivity, -np.cumsum(Model_pred.thickness), '-b')
            
        else:
            self.Appres_curve.set_ydata(Data_pred.appres)
            self.Phase_curve.set_ydata(Data_pred.phase)
            self.Resistivity_plot.set_xdata(Model_pred.resistivity)

        # print(i)
        self.fig.canvas.draw()
        plt.pause(0.01)
        # return self.fig
def forwardMT(resistivity, thickness, frequency):
    # the resistivity shouldnt in logarithmic scale, use np.exp before put the resistivity on this function
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
    # the inputed resistivity should be on logarithmic scale
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