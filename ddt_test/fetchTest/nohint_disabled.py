import pandas as pd
import matplotlib.pyplot as plt

col=['1', '2']

t1 = pd.read_csv('nhwg_disabled.txt', sep=' ', names=col).iloc[:, -1]
t2 = pd.read_csv('nhwog_disabled.txt', sep=' ', names=col).iloc[:, -1]

axis = []
[ axis.append(x) for x in range(20000) ]

fig, (ax2, ax3) = plt.subplots(2, sharex=True, sharey=True)
#fig.tight_layout()

ax2.plot(t1[:10000])
ax3.plot(t2[:10000])

ax3.set_xlabel("# of doubles")
ax2.set_ylabel("cycles")
ax2.set_title("no prefetch with a bunch calculation")
ax3.set_title("no prefetch without calculation")
ax3.set_ylabel("cycles")

fig.subplots_adjust(hspace=.3)
fig.suptitle('nohint w/o calculation hardware prefetch disabled')

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
