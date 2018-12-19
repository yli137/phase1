import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
from scipy.fftpack import fft, ifft

col=['1', '2', '3']
#t0 = pd.read_csv('upfrontplainwogoof_t0.txt', sep=' ', names=col).iloc[:, -1]
#t1 = pd.read_csv('upfrontplainwogoof_t1.txt', sep=' ', names=col).iloc[:, -1]
#t2 = pd.read_csv('upfrontplainwogoof_t2.txt', sep=' ', names=col).iloc[:, -1]

t0 = pd.read_csv('enabled/ufwg_t0_enabled.txt', sep=' ', names=col).iloc[:, -2]
t1 = pd.read_csv('enabled/ufwg_t1_enabled.txt', sep=' ', names=col).iloc[:, -2]
t2 = pd.read_csv('enabled/ufwg_t2_enabled.txt', sep=' ', names=col).iloc[:, -2]

axis = []
[ axis.append(x) for x in range(20000) ]

fig, (ax2, ax3) = plt.subplots(2, sharex=True, sharey=True)
#fig.tight_layout()

ax2.plot(t1[:])
ax3.plot(t2[:])
#ax4.plot(t0[80000:])

#ax4.set_xlabel("# of doubles")
ax2.set_ylabel("cycles")
ax2.set_title("prefetch to cache level 2 and higher")
ax3.set_title("prefetch to cache level 3 and higher")
#ax4.set_title("prefetch to all cache levels")
ax3.set_ylabel("cycles")
#ax4.set_ylabel("cycles")


ax2.set_ylim([0, 100])
ax3.set_ylim([0, 100])
#ax4.set_ylim([0, 80])

fig.subplots_adjust(hspace=.3)
fig.suptitle('prefetch upfront with calculation hardware prefetch enabled')


plt.show()
'''
import numpy as np

fig2, (ax5, ax6) = plt.subplots(2)

xt1 = np.array(t1[:20000])
xt2 = np.array(t2[:20000])

yt1 = fft(xt1)
yt2 = fft(xt2)


for i in range(yt1.size):
    if yt1[i] < 100000:
        yt1[i] = 0
    if yt2[i] < 100000:
        yt2[i] = 0

yt1inv = ifft(yt1)
yt2inv = ifft(yt2)


ax5.plot(yt1/20000)
ax6.plot(yt2/20000)

#plt.show()

#t1 and t2, med
l1_t1, l2_t2 = [], []
inter = 0
for i in range(t1.size):
    if t1[i] > 2*med and t1[i] < 100:
        print(i - inter)
        inter = i

'''

