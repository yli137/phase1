import pandas as pd
import matplotlib.pyplot as plt

col=['1', '2']
#t0 = pd.read_csv('upfrontplainwogoof_t0.txt', sep=' ', names=col).iloc[:, -1]
#t1 = pd.read_csv('upfrontplainwogoof_t1.txt', sep=' ', names=col).iloc[:, -1]
#t2 = pd.read_csv('upfrontplainwogoof_t2.txt', sep=' ', names=col).iloc[:, -1]

t0 = pd.read_csv('ufs_t0_disabled.txt', sep=' ', names=col).iloc[:, -1]
t1 = pd.read_csv('ufs_t1_disabled.txt', sep=' ', names=col).iloc[:, -1]
t2 = pd.read_csv('ufs_t2_disabled.txt', sep=' ', names=col).iloc[:, -1]

axis = []
[ axis.append(x) for x in range(20000) ]

fig, (ax2, ax3, ax4) = plt.subplots(3, sharex=True, sharey=True)
#fig.tight_layout()

ax2.plot(t1[:20000])
ax3.plot(t2[:20000])
ax4.plot(t0[:20000])

ax4.set_xlabel("# of doubles")
ax2.set_ylabel("cycles")
ax2.set_title("prefetch to cache level 2 and higher")
ax3.set_title("prefetch to cache level 3 and higher")
ax4.set_title("prefetch to all cache levels")
ax3.set_ylabel("cycles")
ax4.set_ylabel("cycles")

fig.subplots_adjust(hspace=.3)
fig.suptitle('prefetch upfront sleep 10 micro seconds hardware prefetch disabled 2nd try')

hist1 = {}
hist2 = {}
for i, j in zip(t1, t2):
    hist1[i] = hist1.get(i, 0) + 1
    hist2[j] = hist2.get(j, 0) + 1

'''
for i in hist1:
    print(i, ":", hist1[i])
'''

plt.show()
