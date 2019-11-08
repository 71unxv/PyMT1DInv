import matplotlib.pyplot as plt 
import numpy as np 
import MT as MT
import copy
def visualizeInv(Data_pred, Model_pred, Data_obs, Model_true, fig, iter=1):
    if iter==1:
        gs = fig.add_gridspec(2, 2)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        
        figAppres = fig.add_subplot(gs[0,0])
        figPhase = fig.add_subplot(gs[1,0])
        figResistivity = fig.add_subplot(gs[0:,1])
        
        figAppres.loglog(frequency, Data_obs.appres, '.r')
        figAppres.grid(b=True, which='minor', color='gray', linestyle='-', linewidth = 0.1)
        figPhase.loglog(frequency, Data_obs.phase, '.r')
        figPhase.grid(b=True, which='minor', color='gray', linestyle='-', linewidth = 0.1)
        
        # if Model_true != 0:
        figResistivity.step(Model_true.resistivity, -np.cumsum(Model_true.thickness), '-r')
        
    

    
        Appres_curve, = figAppres.loglog(Data_obs.frequency, Data_obs.appres)
        Phase_curve, = figPhase.loglog(Data_obs.frequency, Data_obs.phase)
        Resistivity_plot, = figResistivity.step(Model_pred.resistivity, -np.cumsum(Model_pred.thickness), '-k')
        

    else:
        Appres_curve.set_ydata(Data_obs.appres)
        Phase_curve.set_ydata(Data_obs.phase)
        Resistivity_plot.set_xdata(Model_pred.resistivity)

    print(i)
    fig.canvas.draw()
    plt.pause(0.5)
    return fig

frequency = np.logspace(-4,4,100)

resistivity = np.array([100,200,20,1000,200])
thickness = np.array([100,100,100,100,100])

DataMT_obs = MT.Data(frequency)
ModelMT_obs = MT.Model(resistivity, thickness)

DataMT_obs.appres = np.zeros([len(frequency),1])
DataMT_obs.phase = np.zeros([len(frequency),1])

DataMT_obs1 = copy.copy(DataMT_obs)
ModelMT_obs1 = copy.copy(ModelMT_obs)

DataMT_obs2 = copy.copy(DataMT_obs)
ModelMT_obs2 = copy.copy(ModelMT_obs)

DataMT_obs3 = copy.copy(DataMT_obs)
ModelMT_obs3 = copy.copy(ModelMT_obs)

ModelMT_obs1.resistivity[0] = ModelMT_obs1.resistivity[0] *0.8

ModelMT_obs2.resistivity[0] = ModelMT_obs2.resistivity[1] *0.8

ModelMT_obs3.resistivity[0] = ModelMT_obs3.resistivity[2] *0.8


for i in range(len(frequency)):
    DataMT_obs.appres[i], DataMT_obs.phase[i] = MT.forwardMT(ModelMT_obs.resistivity, ModelMT_obs.thickness, DataMT_obs.frequency[i])
    DataMT_obs1.appres[i], DataMT_obs1.phase[i] = MT.forwardMT(ModelMT_obs1.resistivity, ModelMT_obs1.thickness, DataMT_obs1.frequency[i])
    DataMT_obs2.appres[i], DataMT_obs2.phase[i] = MT.forwardMT(ModelMT_obs2.resistivity, ModelMT_obs2.thickness, DataMT_obs2.frequency[i])
    DataMT_obs3.appres[i], DataMT_obs3.phase[i] = MT.forwardMT(ModelMT_obs3.resistivity, ModelMT_obs3.thickness, DataMT_obs3.frequency[i])

    

    
    
plt.ion()
fig = plt.figure()
visualizeInv(Data_pred = DataMT_obs, Model_pred = ModelMT_obs, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=1)

visualizeInv(Data_pred = DataMT_obs1, Model_pred = ModelMT_obs1, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=2)

visualizeInv(Data_pred = DataMT_obs2, Model_pred = ModelMT_obs2, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=3)

visualizeInv(Data_pred = DataMT_obs3, Model_pred = ModelMT_obs3, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=4)
plt.ioff()
plt.show()

    

print(DataMT_obs.appres)


