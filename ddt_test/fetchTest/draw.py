import pandas as pd
import matplotlib.pyplot as plt

col=['1', '2']
t0 = pd.read_csv('waitmult0.txt', sep=' ', names=col).iloc[:, -1]
t1 = pd.read_csv('waitmult1.txt', sep=' ', names=col).iloc[:, -1]
t2 = pd.read_csv('waitmult2.txt', sep=' ', names=col).iloc[:, -1]

axis = []
[ axis.append(x) for x in range(800000) ]

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
ax1.plot(t0[:300])
ax2.plot(t1[:300])
ax3.plot(t2[:300])

ax3.set_xlabel("# of doubles")
ax1.set_ylabel("cycles")
ax2.set_ylabel("cycles")
ax3.set_ylabel("cycles")
ax1.set_title('one prefetch at beginning with 1s sleep')

plt.show()
