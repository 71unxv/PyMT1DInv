import matplotlib.pyplot as plt 
import numpy as np 
from MT import MT
from MT.Visualize import Visualize
import copy


frequency = np.logspace(-4,4,100)

resistivity = np.array([100,200,20,1000,200])
thickness = np.array([100,100,100,100,100])

DataMT_obs = MT.Data(frequency)
ModelMT_obs = MT.Model(resistivity, thickness)

DataMT_obs.appres = np.zeros([len(frequency),1])
DataMT_obs.phase = np.zeros([len(frequency),1])

DataMT_obs1 = copy.deepcopy(DataMT_obs)
ModelMT_obs1 = copy.deepcopy(ModelMT_obs)

DataMT_obs2 = copy.deepcopy(DataMT_obs)
ModelMT_obs2 = copy.deepcopy(ModelMT_obs)

DataMT_obs3 = copy.deepcopy(DataMT_obs)
ModelMT_obs3 = copy.deepcopy(ModelMT_obs)
ModelMT_obs3.resistivity = np.array([100,200,20,10,200])
ModelMT_obs1.resistivity[0] = ModelMT_obs1.resistivity[0] *0.5

ModelMT_obs2.resistivity[1] = ModelMT_obs2.resistivity[1] *0.5

ModelMT_obs3.resistivity[2] = ModelMT_obs3.resistivity[2] *0.5


for i in range(len(frequency)):
    DataMT_obs.appres[i], DataMT_obs.phase[i] = MT.forwardMT(ModelMT_obs.resistivity, ModelMT_obs.thickness, DataMT_obs.frequency[i])
    DataMT_obs1.appres[i], DataMT_obs1.phase[i] = MT.forwardMT(ModelMT_obs1.resistivity, ModelMT_obs1.thickness, DataMT_obs1.frequency[i])
    DataMT_obs2.appres[i], DataMT_obs2.phase[i] = MT.forwardMT(ModelMT_obs2.resistivity, ModelMT_obs2.thickness, DataMT_obs2.frequency[i])
    DataMT_obs3.appres[i], DataMT_obs3.phase[i] = MT.forwardMT(ModelMT_obs3.resistivity, ModelMT_obs3.thickness, DataMT_obs3.frequency[i])

    

    
    
plt.ion()
# fig = plt.figure()
# visualizeInv(Data_pred = DataMT_obs, Model_pred = ModelMT_obs, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=1)

# visualizeInv(Data_pred = DataMT_obs1, Model_pred = ModelMT_obs1, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=2)

# visualizeInv(Data_pred = DataMT_obs2, Model_pred = ModelMT_obs2, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=3)

# visualizeInv(Data_pred = DataMT_obs3, Model_pred = ModelMT_obs3, Data_obs = DataMT_obs, Model_true = ModelMT_obs, fig=fig, iter=4)

figureInv = Visualize()

figureInv.plot_Data_obs(DataMT_obs)
figureInv.plot_Model_true(ModelMT_obs)

figureInv.plot_Inv(DataMT_obs1, ModelMT_obs1, iter=1)

figureInv.plot_Inv(DataMT_obs2, ModelMT_obs2, iter=2)

figureInv.plot_Inv(DataMT_obs3, ModelMT_obs3, iter=3)
figureInv.plot_Inv(DataMT_obs1, ModelMT_obs1, iter=4)

figureInv.plot_Inv(DataMT_obs2, ModelMT_obs2, iter=5)

figureInv.plot_Inv(DataMT_obs3, ModelMT_obs3, iter=6)
figureInv.plot_Inv(DataMT_obs1, ModelMT_obs1, iter=4)

figureInv.plot_Inv(DataMT_obs2, ModelMT_obs2, iter=5)

figureInv.plot_Inv(DataMT_obs3, ModelMT_obs3, iter=6)


plt.ioff()
plt.show()

    

# print(DataMT_obs.appres)


