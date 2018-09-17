import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

col = ['1','2','3','4']

mem1 = pd.read_csv('../actualMemcpy/memcpy1_2.txt', sep=' ', names=col)
mem2 = pd.read_csv('../actualMemcpy/memcpy2_2.txt', sep=' ', names=col)
mem3 = pd.read_csv('../actualMemcpy/memcpy3_2.txt', sep=' ', names=col)
mem4 = pd.read_csv('../actualMemcpy/memcpy4_2.txt', sep=' ', names=col)
mem5 = pd.read_csv('../actualMemcpy/memcpy5_2.txt', sep=' ', names=col)
mem6 = pd.read_csv('../actualMemcpy/memcpy6_2.txt', sep=' ', names=col)
mem7 = pd.read_csv('../actualMemcpy/memcpy7_2.txt', sep=' ', names=col)
mem8 = pd.read_csv('../actualMemcpy/memcpy8_2.txt', sep=' ', names=col)

_1t0 = pd.read_csv('1hintT0_2.txt', sep=' ', names=col)
_2t0 = pd.read_csv('2hintT0_2.txt', sep=' ', names=col)
_3t0 = pd.read_csv('3hintT0_2.txt', sep=' ', names=col)
_4t0 = pd.read_csv('4hintT0_2.txt', sep=' ', names=col)
_5t0 = pd.read_csv('5hintT0_2.txt', sep=' ', names=col)
_6t0 = pd.read_csv('6hintT0_2.txt', sep=' ', names=col)
_7t0 = pd.read_csv('7hintT0_2.txt', sep=' ', names=col)
_8t0 = pd.read_csv('8hintT0_2.txt', sep=' ', names=col)

_1t1 = pd.read_csv('../hintT1mem/1hintT1_2.txt', sep=' ', names=col)
_2t1 = pd.read_csv('../hintT1mem/2hintT1_2.txt', sep=' ', names=col)
_3t1 = pd.read_csv('../hintT1mem/3hintT1_2.txt', sep=' ', names=col)
_4t1 = pd.read_csv('../hintT1mem/4hintT1_2.txt', sep=' ', names=col)
_5t1 = pd.read_csv('../hintT1mem/5hintT1_2.txt', sep=' ', names=col)
_6t1 = pd.read_csv('../hintT1mem/6hintT1_2.txt', sep=' ', names=col)
_7t1 = pd.read_csv('../hintT1mem/7hintT1_2.txt', sep=' ', names=col)
_8t1 = pd.read_csv('../hintT1mem/8hintT1_2.txt', sep=' ', names=col)

_1t2 = pd.read_csv('../hintT2mem/1hintT2_2.txt', sep=' ', names=col)
_2t2 = pd.read_csv('../hintT2mem/2hintT2_2.txt', sep=' ', names=col)
_3t2 = pd.read_csv('../hintT2mem/3hintT2_2.txt', sep=' ', names=col)
_4t2 = pd.read_csv('../hintT2mem/4hintT2_2.txt', sep=' ', names=col)
_5t2 = pd.read_csv('../hintT2mem/5hintT2_2.txt', sep=' ', names=col)
_6t2 = pd.read_csv('../hintT2mem/6hintT2_2.txt', sep=' ', names=col)
_7t2 = pd.read_csv('../hintT2mem/7hintT2_2.txt', sep=' ', names=col)
_8t2 = pd.read_csv('../hintT2mem/8hintT2_2.txt', sep=' ', names=col)

memsize = mem1.iloc[:, 0]+mem2.iloc[:, 0]+mem3.iloc[:, 0]+mem4.iloc[:, 0]+mem5.iloc[:, 0]+mem6.iloc[:, 0]+mem7.iloc[:, 0]+mem8.iloc[:, 0]
memchunk = mem1.iloc[:, 1]+mem2.iloc[:, 1]+mem3.iloc[:, 1]+mem4.iloc[:, 1]+mem5.iloc[:, 1]+mem6.iloc[:, 1]+mem7.iloc[:, 1]+mem8.iloc[:, 1]
memspeed = mem1.iloc[:, 2]+mem2.iloc[:, 2]+mem3.iloc[:, 2]+mem4.iloc[:, 2]+mem5.iloc[:, 2]+mem6.iloc[:, 2]+mem7.iloc[:, 2]+mem8.iloc[:, 2]

t0size = _1t0.iloc[:, 0] + _2t0.iloc[:, 0] +_3t0.iloc[:, 0] + _4t0.iloc[:, 0]+_5t0.iloc[:, 0] + _6t0.iloc[:, 0] +_7t0.iloc[:, 0] + _8t0.iloc[:, 0]
t1size = _1t1.iloc[:, 0] + _2t1.iloc[:, 0] +_3t1.iloc[:, 0] + _4t1.iloc[:, 0]+_5t1.iloc[:, 0] + _6t1.iloc[:, 0] +_7t1.iloc[:, 0] + _8t1.iloc[:, 0]
t2size = _1t2.iloc[:, 0] + _2t2.iloc[:, 0] +_3t2.iloc[:, 0] + _4t2.iloc[:, 0]+_5t2.iloc[:, 0] + _6t2.iloc[:, 0] +_7t2.iloc[:, 0] + _8t2.iloc[:, 0]

t0chunk = _1t0.iloc[:, 1] + _2t0.iloc[:, 1] +_3t0.iloc[:, 1] + _4t0.iloc[:, 1]+_5t0.iloc[:, 1] + _6t0.iloc[:, 1] +_7t0.iloc[:, 1] + _8t0.iloc[:, 1]
t1chunk = _1t1.iloc[:, 1] + _2t1.iloc[:, 1] +_3t1.iloc[:, 1] + _4t1.iloc[:, 1]+_5t1.iloc[:, 1] + _6t1.iloc[:, 1] +_7t1.iloc[:, 1] + _8t1.iloc[:, 1]
t2chunk = _1t2.iloc[:, 1] + _2t2.iloc[:, 1] +_3t2.iloc[:, 1] + _4t2.iloc[:, 1]+_5t2.iloc[:, 1] + _6t2.iloc[:, 1] +_7t2.iloc[:, 1] + _8t2.iloc[:, 1]

t0speed = _1t0.iloc[:, 2] + _2t0.iloc[:, 2] +_3t0.iloc[:, 2] + _4t0.iloc[:, 2]+_5t0.iloc[:, 2] + _6t0.iloc[:, 2] +_7t0.iloc[:, 2] + _8t0.iloc[:, 2]
t1speed = _1t1.iloc[:, 2] + _2t1.iloc[:, 2] +_3t1.iloc[:, 2] + _4t1.iloc[:, 2]+_5t1.iloc[:, 2] + _6t1.iloc[:, 2] +_7t1.iloc[:, 2] + _8t1.iloc[:, 2]
t2speed = _1t2.iloc[:, 2] + _2t2.iloc[:, 2] +_3t2.iloc[:, 2] + _4t2.iloc[:, 2]+_5t2.iloc[:, 2] + _6t2.iloc[:, 2] +_7t2.iloc[:, 2] + _8t2.iloc[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(memsize, memchunk, memspeed)
ax.scatter(t0size, t0chunk, t0speed)
ax.scatter(t1size, t1chunk, t1speed)
ax.scatter(t2size, t2chunk, t2speed)

ax.set_xlabel('outputsize')
ax.set_ylabel('inputsize')
ax.set_zlabel('bandwidth')

ax.legend(['no hint', 'T0', 'T1', 'T2'])

plt.show()
