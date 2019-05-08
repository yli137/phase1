import pandas as pd
import matplotlib.pyplot as plt

col=['1', '2', '3']

t1 = pd.read_csv('enabled/nhwog_enabled.txt', sep=' ', names=col).iloc[:, -2]
t2 = pd.read_csv('disabled/nhwog_disabled.txt', sep=' ', names=col).iloc[:, -2]

axis = []
[ axis.append(x) for x in range(20000) ]

fig, (ax2, ax3) = plt.subplots(2, sharex=True, sharey=True)
#fig.tight_layout()

ax2.plot(t1)
ax3.plot(t2)

ax3.set_xlabel("# of doubles")
ax2.set_ylabel("cycles")
ax2.set_title("no prefetch hardware prefetch enabled")
ax3.set_title("no prefetch hardware prefetch disabled")
ax3.set_ylabel("cycles")

ax2.set_ylim([-3, 40])
ax3.set_ylim([-3, 40])


fig.subplots_adjust(hspace=.3)
fig.suptitle('nohint w/o hardware prefetch')
#plt.show()

t3 = []
for a,b in zip(t1, t2):
    t3.append(a-b)

fig2, (ax5) = plt.subplots(1)
ax5.plot(t3)
plt.show()

'''
import numpy as np
from scipy.fftpack import fft, ifft
fig2, (ax5, ax6) = plt.subplots(2)
xt1 = np.array(t1)
xt2 = np.array(t2)

yt1 = fft(xt1)
yt2 = fft(xt2)

ax5.plot(yt1/80000)
ax6.plot(yt2/80000)

plt.show()
'''
