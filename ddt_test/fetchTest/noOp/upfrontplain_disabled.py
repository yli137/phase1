import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
from scipy.fftpack import fft, ifft

col=['1', '2']
#t0 = pd.read_csv('upfrontplainwogoof_t0.txt', sep=' ', names=col).iloc[:, -1]
#t1 = pd.read_csv('upfrontplainwogoof_t1.txt', sep=' ', names=col).iloc[:, -1]
#t2 = pd.read_csv('upfrontplainwogoof_t2.txt', sep=' ', names=col).iloc[:, -1]

t0 = pd.read_csv('ufp_t0_disabled.txt', sep=' ', names=col).iloc[:, -1]
t1 = pd.read_csv('ufp_t1_disabled.txt', sep=' ', names=col).iloc[:, -1]
t2 = pd.read_csv('ufp_t2_disabled.txt', sep=' ', names=col).iloc[:, -1]

med = stat.median(t1)

axis = []
[ axis.append(x) for x in range(20000) ]

fig, (ax2, ax3) = plt.subplots(2, sharex=True, sharey=True)
#fig.tight_layout()

ax2.plot(t1[:])
ax3.plot(t2[:])

#ax4.set_xlabel("# of doubles")
ax2.set_ylabel("cycles")
ax2.set_title("prefetch to cache level 2 and higher")
ax3.set_title("prefetch to cache level 3 and higher")
#ax4.set_title("prefetch to all cache levels")
ax3.set_ylabel("cycles")
#ax4.set_ylabel("cycles")

ax2.set_ylim([0, 1000])
ax3.set_ylim([0, 1000])

fig.subplots_adjust(hspace=.3)
fig.suptitle('prefetch upfront plain hardware prefetch disabled 2nd try')

import numpy as np

fig2, (ax5, ax6) = plt.subplots(2)

xt1 = np.array(t1[:20000])
xt2 = np.array(t2[:20000])

yt1 = fft(xt1)
yt2 = fft(xt2)


for i in range(yt1.size):
    if abs(yt1[i]) < 1000:
        yt1[i] = 0
    if abs(yt2[i]) < 1000:
        yt2[i] = 0

yt1inv = ifft(yt1)
yt2inv = ifft(yt2)

print(max(xt1))
ax5.plot(yt1inv)
ax6.plot(yt2inv)

print(yt1)
print(yt2)

plt.show()
