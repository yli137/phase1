import pandas as pd
import matplotlib.pyplot as plt

col=['1', '2', '3']

t1 = pd.read_csv('enabled_time/nohint.txt', sep=' ', names=col).iloc[:, -2]
t2 = pd.read_csv('disabled_time/nohint.txt', sep=' ', names=col).iloc[:, -2]

axis = []
[ axis.append(x) for x in range(20000) ]

fig, (ax2, ax3) = plt.subplots(2, sharex=True, sharey=True)
#fig.tight_layout()

ax2.plot(t1[:-1])
ax3.plot(t2[:-1])

ax3.set_xlabel("# of doubles")
ax2.set_ylabel("cycles")
ax2.set_title("no prefetch hardware prefetch enabled")
ax3.set_title("no prefetch hardware prefetch disabled")
ax3.set_ylabel("time (s)")

fig.subplots_adjust(hspace=.3)
fig.suptitle('nohint w/o hardware prefetch')

fig3, (ax6, ax7) = plt.subplots(2, sharex=True, sharey=True)
ax6.plot(t1[:-1])
ax6.set_title("disabled hinted")
ax7.plot(t2[:-1])
ax7.set_title("disabled nohint")
ax7.set_ylabel("seconds")
ax7.set_xlabel("# of doubles")

time1 = sum(t1[:-1])
time2 = sum(t2[:-1])
print('enabled total time =', time1 * 1000000, 'micro seconds')
print('disabled total time =', time2 * 1000000, 'micro seconds')

plt.show()


