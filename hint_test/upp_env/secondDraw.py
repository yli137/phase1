import pandas as pd
import matplotlib.pyplot as plt

col = ['0','1','2','3','4','5','6','7','8','9','11','22','33']
nohint = pd.read_csv('nohintdata.txt', sep=' ', names=col)
hint0 = pd.read_csv('hintdataT0Second.txt', sep=' ', names=col)
hint1 = pd.read_csv('hintdataT1Second.txt', sep=' ', names=col)
hint2 = pd.read_csv('hintdataT2Second.txt', sep=' ', names=col)

inputsize = nohint.iloc[:, 3] + hint0.iloc[:, 3] + hint1.iloc[:, 3]\
             +hint2.iloc[:, 3]
speed = nohint.iloc[:, -2] + hint0.iloc[:, -2] + hint1.iloc[:, -2]\
             +hint2.iloc[:, -2]

nohintsize = nohint.iloc[:, 1]
hint0size = hint0.iloc[:, 1]
hint1size = hint1.iloc[:, 1]
hint2size = hint2.iloc[:, 1]

nohintsize = [x*8/1000000 for x in nohintsize]
hint0size = [x*8/1000000 for x in hint0size]
hint1size = [x*8/1000000 for x in hint1size]
hint2size = [x*8/1000000 for x in hint2size]

nohintin = nohint.iloc[:, 3]
hint0in = hint0.iloc[:, 3]
hint1in = hint1.iloc[:, 3]
hint2in = hint2.iloc[:, 3]

nohintspeed = nohint.iloc[:, -2]
hint0speed = hint0.iloc[:, -2]
hint1speed = hint1.iloc[:, -2]
hint2speed = hint2.iloc[:, -2]

density = [x/y for x,y in zip(nohintsize, nohintin)]
density0 = [x/y for x,y in zip(hint0size, hint0in)]
density1 = [x/y for x,y in zip(hint1size, hint1in)]
density2 = [x/y for x,y in zip(hint2size, hint2in)]

cut = 14
xupper = 20
ylower, yupper = 10, 12.5
fig, ax = plt.subplots(2, 4)
ax[0,0].set_ylim(ylower, yupper)
ax[0,0].set_xlim(0, xupper)
ax[0,1].set_ylim(ylower, yupper)
ax[0,1].set_xlim(0, xupper)
ax[0,2].set_ylim(ylower, yupper)
ax[0,2].set_xlim(0, xupper)
ax[0,3].set_ylim(ylower, yupper)
ax[0,3].set_xlim(0, xupper)
ax[1,0].set_ylim(ylower, yupper)
ax[1,0].set_xlim(0, xupper)
ax[1,1].set_ylim(ylower, yupper)
ax[1,1].set_xlim(0, xupper)
ax[1,2].set_ylim(ylower, yupper)
ax[1,2].set_xlim(0, xupper)
ax[1,3].set_ylim(ylower, yupper)
ax[1,3].set_xlim(0, xupper)

ax[0, 0].plot(nohintsize[:cut], nohintspeed[:cut])
ax[0, 1].plot(nohintsize[cut:2*cut], nohintspeed[cut:2*cut])
ax[0, 2].plot(nohintsize[2*cut:3*cut], nohintspeed[2*cut:3*cut])
ax[0, 3].plot(nohintsize[3*cut:4*cut], nohintspeed[3*cut:4*cut])
ax[1, 0].plot(nohintsize[4*cut:5*cut], nohintspeed[4*cut:5*cut])
ax[1, 1].plot(nohintsize[5*cut:6*cut], nohintspeed[5*cut:6*cut])
ax[1, 2].plot(nohintsize[6*cut:7*cut], nohintspeed[6*cut:7*cut])
ax[1, 3].plot(nohintsize[7*cut:8*cut], nohintspeed[7*cut:8*cut])

ax[0, 0].plot(hint0size[:cut], hint0speed[:cut])
ax[0, 1].plot(hint0size[cut:2*cut], hint0speed[cut:2*cut])
ax[0, 2].plot(hint0size[2*cut:3*cut], hint0speed[2*cut:3*cut])
ax[0, 3].plot(hint0size[3*cut:4*cut], hint0speed[3*cut:4*cut])
ax[1, 0].plot(hint0size[4*cut:5*cut], hint0speed[4*cut:5*cut])
ax[1, 1].plot(hint0size[5*cut:6*cut], hint0speed[5*cut:6*cut])
ax[1, 2].plot(hint0size[6*cut:7*cut], hint0speed[6*cut:7*cut])
ax[1, 3].plot(hint0size[7*cut:8*cut], hint0speed[7*cut:8*cut])

ax[0, 0].plot(hint1size[:cut], hint1speed[:cut])
ax[0, 1].plot(hint1size[cut:2*cut], hint1speed[cut:2*cut])
ax[0, 2].plot(hint1size[2*cut:3*cut], hint1speed[2*cut:3*cut])
ax[0, 3].plot(hint1size[3*cut:4*cut], hint1speed[3*cut:4*cut])
ax[1, 0].plot(hint1size[4*cut:5*cut], hint1speed[4*cut:5*cut])
ax[1, 1].plot(hint1size[5*cut:6*cut], hint1speed[5*cut:6*cut])
ax[1, 2].plot(hint1size[6*cut:7*cut], hint1speed[6*cut:7*cut])
ax[1, 3].plot(hint1size[7*cut:8*cut], hint1speed[7*cut:8*cut])

ax[0, 0].plot(hint2size[:cut], hint2speed[:cut])
ax[0, 1].plot(hint2size[cut:2*cut], hint2speed[cut:2*cut])
ax[0, 2].plot(hint2size[2*cut:3*cut], hint2speed[2*cut:3*cut])
ax[0, 3].plot(hint2size[3*cut:4*cut], hint2speed[3*cut:4*cut])
ax[1, 0].plot(hint2size[4*cut:5*cut], hint2speed[4*cut:5*cut])
ax[1, 1].plot(hint2size[5*cut:6*cut], hint2speed[5*cut:6*cut])
ax[1, 2].plot(hint2size[6*cut:7*cut], hint2speed[6*cut:7*cut])
ax[1, 3].plot(hint2size[7*cut:8*cut], hint2speed[7*cut:8*cut])

ax[0,0].set_xlabel('size (MB)')
ax[0,0].set_ylabel('Bandwidth (GBps)')
plt.legend(['nohint', 'hint T0', 'hint T1', 'hint T2'], bbox_to_anchor=(1.1, 1.05))

plt.tight_layout()
plt.show()
