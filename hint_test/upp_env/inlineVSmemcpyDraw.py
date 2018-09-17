import pandas as pd
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots(2, 4)
ax[0, 0].plot(mem1size, mem1speed, label='hint', color='b')
ax[0, 1].plot(mem2size, mem2speed, label='hint', color='b')
ax[0, 2].plot(mem3size, mem3speed, label='hint', color='b')
ax[0, 3].plot(mem4size, mem4speed, label='hint', color='b')
ax[1, 0].plot(mem5size, mem5speed, label='hint', color='b')
ax[1, 1].plot(mem6size, mem6speed, label='hint', color='b')
ax[1, 2].plot(mem7size, mem7speed, label='hint', color='b')
ax[1, 3].plot(mem8size, mem8speed, label='hint', color='b')

ax[0, 0].plot(mem1size, inline1speed, label="w/o hint", color='r')
ax[0, 1].plot(mem2size, inline2speed, label="w/o hint", color='r')
ax[0, 2].plot(mem3size, inline3speed, label="w/o hint", color='r')
ax[0, 3].plot(mem4size, inline4speed, label="w/o hint", color='r')
ax[1, 0].plot(mem5size, inline5speed, label="w/o hint", color='r')
ax[1, 1].plot(mem6size, inline6speed, label="w/o hint", color='r')
ax[1, 2].plot(mem7size, inline7speed, label="w/o hint", color='r')
ax[1, 3].plot(mem8size, inline8speed, label="w/o hint", color='r')

plt.legend(['memcpy', 'inlined memcpy'], bbox_to_anchor=(1.1, 1.05))
plt.suptitle('memcpy vs. inline memcpy')

plt.show()
