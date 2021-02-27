import numpy as np 
import plotly.graph_objects as go
import matplotlib.pyplot as plt 

# def get_x_y_steps(x, y, where="post"):
#     if where == "post":
#         x_step = [x[0]] + [_x for tup in zip(x, x)[1:] for _x in tup]
#         y_step = [_y for tup in zip(y, y)[:-1] for _y in tup] + [y[-1]]
#     elif where == "pre":
#         x_step = [_x for tup in zip(x, x)[:-1] for _x in tup] + [x[-1]]
#         y_step = [y[0]] + [_y for tup in zip(y, y)[1:] for _y in tup]
#     return x_step, y_step


def getStairData(x,y):
    X_Stair = []
    Y_Stair = []
    for i in range(len(y)):
        X_Stair.append(x[i])
        X_Stair.append(x[i])
        if i == 0:
            Y_Stair.append(0)
            Y_Stair.append(y[i])
        else:
            Y_Stair.append(y[i-1])
            Y_Stair.append(y[i])
    return X_Stair, Y_Stair


Thickness = -np.array([100,200,400,100,500,200])
Resistivity = np.array([100,200,40,10,300,500])

Depth = np.cumsum(Thickness)
X_Stair, Y_Stair = getStairData(Resistivity,Depth)
# plt.plot(X_Stair, Y_Stair, '-*')
# plt.plot(Resistivity,Depth, 'o')

# plt.show()

#%
import plotly.graph_objects as go


x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 3, 1])

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=X_Stair, 
                y=Y_Stair, 
                name="True Resistivity",
                line_shape='linear')
                )

fig.update_traces(hoverinfo='text+name', mode='lines')
# fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))

fig.show()