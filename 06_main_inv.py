import numpy as np 
import matplotlib.pyplot as plt 
# from PyMT1D import Model, Data, Visualize
import PyMT1D
from scipy.sparse.linalg import lsqr, bicg, bicgstab


frequency = np.logspace(-4,4,100)
resistivity = np.log(np.array([100,100,400,800,1000]))
thickness = np.array([400,400,400,400,400])



DataMT_obs = PyMT1D.Data(frequency)
ModelMT_true = PyMT1D.Model(resistivity, thickness)

DataMT_obs.appres = np.zeros(len(DataMT_obs.frequency))
DataMT_obs.phase = np.zeros(len(DataMT_obs.frequency))

for freq in range(len(DataMT_obs.frequency)):
    DataMT_obs.appres[freq], DataMT_obs.phase[freq] = PyMT1D.forwardMT(np.exp(ModelMT_true.resistivity), ModelMT_true.thickness, DataMT_obs.frequency[freq])

plt.ion()
PyMT1Dplot = PyMT1D.Visualize()
PyMT1Dplot.plot_Data_obs(DataMT_obs)
PyMT1Dplot.plot_Model_true(ModelMT_true)

max_iter = 15



# initial_model

resistivity_init = np.log(np.array([100,100,100,100,100]))
thickness_init = np.array([400,400,400,400,400])

ModelMT_init = PyMT1D.Model(resistivity_init, thickness_init)
DataMT_pred = PyMT1D.Data(frequency)
DataMT_pred.appres = np.zeros(len(DataMT_pred.frequency))
DataMT_pred.phase = np.zeros(len(DataMT_pred.frequency))

Wm = np.eye(len(ModelMT_init.resistivity))
beta = 1
# Total = np.vstack([a,b])

for iter in range(1,max_iter+1):
    if iter >= max_iter/2:
        beta = 0.5
    
    

    for freq in range(len(DataMT_obs.frequency)):
        DataMT_pred.appres[freq], DataMT_pred.phase[freq] = PyMT1D.forwardMT(np.exp(ModelMT_init.resistivity), ModelMT_init.thickness, DataMT_pred.frequency[freq])
    PyMT1Dplot.plot_Inv(DataMT_pred, ModelMT_init, iter=iter)
    
    
    
    d_app = np.log(DataMT_obs.appres[:, None]) - np.log(DataMT_pred.appres[:, None]) 
    d_phs = np.log(DataMT_obs.phase[:, None]) - np.log(DataMT_pred.phase[:, None])
    df = np.vstack([d_app, d_phs])

    RMSE = np.sqrt(np.dot(df.T,df))
    print("Iterasi ke - " + str(iter) + "  | RMSE: " + str(RMSE))
    # print(RMSE)

            #   d1=log(d_obs_app)-log(d_cal_app(:,iter));
            #   d2=log(d_obs_phase)-log(d_cal_phase(:,iter));
            #   df=[d1;d2];
            #   RMSE=sqrt(df'*df);


    J_app, J_phs = PyMT1D.jacobianMT(DataMT_obs.frequency, ModelMT_init.resistivity, ModelMT_init.thickness)

    J = np.vstack([J_app, J_phs])

    tes = np.dot(J.T,J)
    # print(J.shape)
    # print(tes.shape)
    # J'*J
    # print(J.shape)
    # print(df.shape)

    A = np.dot(J.T,J) + (Wm*(beta**2))
    b = np.dot(J.T,df)

    dm = lsqr(A,b)

    ModelMT_init.resistivity = ModelMT_init.resistivity - dm[0]









plt.ioff()
plt.show()

