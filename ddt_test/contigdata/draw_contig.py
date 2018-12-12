import pandas as pd
import matplotlib.pyplot as plt

size = [1, 64, 512, 1024, 2048, 4096, 8192]
#size to MB
size = [x * 8 / 1000000 for x in size]

col = ['1','2','3','4','5','6','7','8']
data = pd.read_csv('contigdata.txt', sep=' ', names=col)
cptime = data.iloc[:, -4]

bandwidth = [x/y for x,y in zip(size, cptime)]

plt.plot(size, bandwidth)

plt.show()
