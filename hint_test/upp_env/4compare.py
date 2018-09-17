import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

col = ['0', '1','2','3','4','5','6','7','8','9','11']

h0 = pd.read_csv('hintdataT0.txt', sep=' ', names = col)
h1 = pd.read_csv('hintdataT1.txt', sep=' ', names = col)
h2 = pd.read_csv('hintdataT2.txt', sep=' ', names = col)
nh = pd.read_csv('nohintdata.txt', sep=' ', names = col)

h0size = h0.iloc[:, 1]
h0chunk = h0.iloc[:, 3]
h0speed = h0.iloc[:, 9]

h1size = h1.iloc[:, 1]
h1chunk = h1.iloc[:, 3]
h1speed = h1.iloc[:, 9]

h2size = h2.iloc[:, 1]
h2chunk = h2.iloc[:, 3]
h2speed = h2.iloc[:, 9]

nhsize = nh.iloc[:, 1]
nhchunk = nh.iloc[:, 3]
nhspeed = nh.iloc[:, 9]

h0size = [x * 8 / 1000000 for x in h0size]
h0chunk = [x * 8 / 1000000 for x in h0chunk]
h1size = [x * 8 / 1000000 for x in h1size]
h1chunk = [x * 8 / 1000000 for x in h1chunk]
h2size = [x * 8 / 1000000 for x in h2size]
h2chunk = [x * 8 / 1000000 for x in h2chunk]
nhsize = [x * 8 / 1000000 for x in nhsize]
nhchunk = [x * 8 / 1000000 for x in nhchunk]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(h0size, h0chunk, h0speed)
ax.scatter(h1size, h1chunk, h1speed)
ax.scatter(h2size, h2chunk, h2speed)
ax.scatter(nhsize, nhchunk, nhspeed)

ax.set_xlabel('outputsize (MB)')
ax.set_ylabel('inputsize (MB)')
ax.set_zlabel('bandwidth (GBps)')

ax.legend(['hint T0', 'hint T1', 'hint T2', 'no hint'])

plt.show()
