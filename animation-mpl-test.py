# import matplotlib.pyplot as plt
# import numpy as np

# import time

# plt.ion()
# for i in range(15):
#     y = np.random.random([10,1])
#     plt.clf()
#     plt.plot(y)
#     plt.plot(y + 4)
#     plt.draw()
#     # time.sleep(1)

#     plt.pause(0.000000001)
# plt.ioff()  
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

plt.ion()
fig = plt.figure()
# fig2 = plt.figure()
# fig.ion()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

line1, = ax.plot(x, y, 'b-')
line2, = ax2.plot(x, y, 'b-')

for phase in np.linspace(0, 10*np.pi, 100):
    line1.set_ydata(np.sin(0.5 * x + phase))
    # fig.canvas.draw()
    # plt.pause(0.1)
    line2.set_ydata(np.sin(0.5 * x + phase))
    fig.canvas.draw()
    plt.pause(0.1)


# for phase in np.linspace(0, 10*np.pi, 100):
#     line2.set_ydata(np.sin(0.5 * x + phase))
#     fig.canvas.draw()
#     plt.pause(0.1)


plt.ioff()
plt.show()