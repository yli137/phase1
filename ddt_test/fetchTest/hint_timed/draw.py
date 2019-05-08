import matplotlib.pyplot as plt
import pandas as pd

col = ['1', '2', '3']
nohint = pd.read_csv('nohint.txt', sep=' ', names=col)
hint0 = pd.read_csv('hint0.txt', sep=' ', names=col)
hint1 = pd.read_csv('hint1.txt', sep=' ', names=col)
hint2 = pd.read_csv('hint2.txt', sep=' ', names=col)


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True, sharey=True)

ax1.plot(nohint.iloc[:,-2])
ax2.plot(hint0.iloc[:,-2])
ax3.plot(hint1.iloc[:,-2])
ax4.plot(hint2.iloc[:,-2])
ax3.set_ylabel('time (s)')
fig.suptitle('nohint hint0 hint1 hint2 time')

fig2, (ax5, ax6, ax7, ax8) = plt.subplots(4, sharex=True, sharey=True)

ax5.plot(nohint.iloc[1:, -1])
ax6.plot(hint0.iloc[1:, -1])
ax7.plot(hint1.iloc[1:, -1])
ax8.plot(hint2.iloc[1:, -1])
fig2.suptitle('timed prefetch nohint hint0 hint1 hint2')


h0, h1, h2 = [], [], []
for x, y in zip(hint0.iloc[:,-1], hint0.iloc[:,-2]):
    h0.append(x+y)

for x, y in zip(hint1.iloc[:,-1], hint1.iloc[:,-2]):
    h1.append(x+y)

for x, y in zip(hint2.iloc[:,-1], hint2.iloc[:,-2]):
    h2.append(x+y)

fig3, (p0, p1, p2, p3) = plt.subplots(4, sharex=True, sharey=True)
p0.plot(nohint.iloc[1:, -2])
p1.plot(h0[1:])
p2.plot(h1[1:])
p2.set_ylabel('time (s)')
p3.plot(h2[1:])
fig3.suptitle('nohint hint0 hint1 hint2 + prefetch time')

print(sum(nohint.iloc[1:, -2]))
print(sum(h0[1:]))
print(sum(h1[1:]))
print(sum(h2[1:]))

plt.show()
