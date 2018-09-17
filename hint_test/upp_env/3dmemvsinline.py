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

inline1 = pd.read_csv('../inlineMem/memcpy1_2.txt', sep=' ', names=col)
inline2 = pd.read_csv('../inlineMem/memcpy2_2.txt', sep=' ', names=col)
inline3 = pd.read_csv('../inlineMem/memcpy3_2.txt', sep=' ', names=col)
inline4 = pd.read_csv('../inlineMem/memcpy4_2.txt', sep=' ', names=col)
inline5 = pd.read_csv('../inlineMem/memcpy5_2.txt', sep=' ', names=col)
inline6 = pd.read_csv('../inlineMem/memcpy6_2.txt', sep=' ', names=col)
inline7 = pd.read_csv('../inlineMem/memcpy7_2.txt', sep=' ', names=col)
inline8 = pd.read_csv('../inlineMem/memcpy8_2.txt', sep=' ', names=col)

mem1size = mem1.iloc[:, 0]
mem2size = mem2.iloc[:, 0]
mem3size = mem3.iloc[:, 0]
mem4size = mem4.iloc[:, 0]
mem5size = mem5.iloc[:, 0]
mem6size = mem6.iloc[:, 0]
mem7size = mem7.iloc[:, 0]
mem8size = mem8.iloc[:, 0]

mem1size = [ x * 8 / 1000000 for x in mem1size ]
mem2size = [ x * 8 / 1000000 for x in mem2size ]
mem3size = [ x * 8 / 1000000 for x in mem3size ]
mem4size = [ x * 8 / 1000000 for x in mem4size ]
mem5size = [ x * 8 / 1000000 for x in mem5size ]
mem6size = [ x * 8 / 1000000 for x in mem6size ]
mem7size = [ x * 8 / 1000000 for x in mem7size ]
mem8size = [ x * 8 / 1000000 for x in mem8size ]

mem1speed = mem1.iloc[:, -2]
mem2speed = mem2.iloc[:, -2]
mem3speed = mem3.iloc[:, -2]
mem4speed = mem4.iloc[:, -2]
mem5speed = mem5.iloc[:, -2]
mem6speed = mem6.iloc[:, -2]
mem7speed = mem7.iloc[:, -2]
mem8speed = mem8.iloc[:, -2]

inline1speed = inline1.iloc[:, -2]
inline2speed = inline2.iloc[:, -2]
inline3speed = inline3.iloc[:, -2]
inline4speed = inline4.iloc[:, -2]
inline5speed = inline5.iloc[:, -2]
inline6speed = inline6.iloc[:, -2]
inline7speed = inline7.iloc[:, -2]
inline8speed = inline8.iloc[:, -2]

memsize = mem1size + mem2size +mem3size+mem4size+mem5size+mem6size+mem7size+mem8size
memspeed = mem1speed+mem2speed+mem3speed+mem4speed+mem5speed+mem6speed+mem7speed+mem8speed
inlinespeed = inline1speed+inline2speed+inline3speed+inline4speed+inline5speed+inline6speed+inline7speed+inline8speed

print(len(memsize))
print(len(memspeed))
print(len(inlinespeed))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(memsize, memspeed)
ax.scatter(memsize, inlinespeed)

plt.legend(['memcpy', 'inlined memcpy'])
plt.suptitle('memcpy vs. inline memcpy')

plt.show()
