import matplotlib.pyplot as plt 
import numpy as np 
import MT as MT
import copy

class Visualize:
        
    def __init__(self, fig=plt.figure()):
        self.fig = fig
        gs = fig.add_gridspec(2, 2)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        
        self.figAppres = self.fig.add_subplot(gs[0,0])
        self.figPhase = self.fig.add_subplot(gs[1,0])
        self.figResistivity = self.fig.add_subplot(gs[0:,1])
    
    def plot_Data_obs(self,Data_obs):
        self.figAppres.loglog(Data_obs.frequency, Data_obs.appres, '.r')
        self.figAppres.grid(b=True, which='minor', color='gray', linestyle='-', linewidth = 0.1)
        self.figPhase.loglog(Data_obs.frequency, Data_obs.phase, '.r')
        self.figPhase.grid(b=True, which='minor', color='gray', linestyle='-', linewidth = 0.1)
    
    def plot_Model_true(self, Model_true):
        # if Model_true != 0:
        self.figResistivity.step(Model_true.resistivity, -np.cumsum(Model_true.thickness), '-r')

    def plot_Inv(self, Data_pred, Model_pred, iter=1):
        if iter==1:
            self.Appres_curve, = self.figAppres.loglog(Data_pred.frequency, Data_pred.appres)
            self.Phase_curve, = self.figPhase.loglog(Data_pred.frequency, Data_pred.phase)
            self.Resistivity_plot, = self.figResistivity.step(Model_pred.resistivity, -np.cumsum(Model_pred.thickness), '-k')
            
        else:
            self.Appres_curve.set_ydata(Data_pred.appres)
            self.Phase_curve.set_ydata(Data_pred.phase)
            self.Resistivity_plot.set_xdata(Model_pred.resistivity)

        # print(i)
        self.fig.canvas.draw()
        plt.pause(0.5)
        # return self.fig