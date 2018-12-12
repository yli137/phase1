import pandas as pd
import matplotlib.pyplot as plt

col = ['1','2','3','4','5','6']
_18 = pd.read_csv('oneeight.txt', sep=' ', names=col)
_28 = pd.read_csv('twoeight.txt', sep=' ', names=col)
_38 = pd.read_csv('threeeight.txt', sep=' ', names=col)
_48 = pd.read_csv('foureight.txt', sep=' ', names=col)
_58 = pd.read_csv('fiveeight.txt', sep=' ', names=col)
_68 = pd.read_csv('sixeight.txt', sep=' ', names=col)
_78 = pd.read_csv('seveneight.txt', sep=' ', names=col)
_88 = pd.read_csv('eighteight.txt', sep=' ', names=col)

_1s = _18.iloc[:, -2]
_2s = _28.iloc[:, -2]
_3s = _38.iloc[:, -2]
_4s = _48.iloc[:, -2]
_5s = _58.iloc[:, -2]
_6s = _68.iloc[:, -2]
_7s = _78.iloc[:, -2]
_8s = _88.iloc[:, -2]

#microseconds to seconds
_1s = [x / 1000000 for x in _1s]
_2s = [x / 1000000 for x in _2s]
_3s = [x / 1000000 for x in _3s]
_4s = [x / 1000000 for x in _4s]
_5s = [x / 1000000 for x in _5s]
_6s = [x / 1000000 for x in _6s]
_7s = [x / 1000000 for x in _7s]
_8s = [x / 1000000 for x in _8s]

#size to megabytes
_1n = [x * 8 /1000 for x in range (1, 40000, 500)]
_2n = [x*2* 8 /1000 for x in range (1, 20000, 437)]
_3n = [x*3* 8 /1000  for x in range (1, 13330, 375)]
_4n = [x*4* 8 /1000  for x in range (1, 10000, 312)]
_5n = [x*5* 8 /1000  for x in range (1, 8000, 250)]
_6n = [x*6* 8 /1000  for x in range (1, 6660, 187)]
_7n = [x*7* 8 /1000  for x in range (1, 5710, 125)]
_8n = [x*8* 8 /1000  for x in range (1, 5000, 62)]

_1band = [x*8/(y/1000) for x,y in zip(_1n, _1s)]
_2band = [x*8/(y/1000) for x,y in zip(_2n, _2s)]
_3band = [x*8/(y/1000) for x,y in zip(_3n, _3s)]
_4band = [x*8/(y/1000) for x,y in zip(_4n, _4s)]
_5band = [x*8/(y/1000) for x,y in zip(_5n, _5s)]
_6band = [x*8/(y/1000) for x,y in zip(_6n, _6s)]
_7band = [x*8/(y/1000) for x,y in zip(_7n, _7s)]
_8band = [x*8/(y/1000) for x,y in zip(_8n, _8s)]

plt.plot(_1n, _1band)
plt.plot(_2n, _2band)
plt.plot(_3n, _3band)
plt.plot(_4n, _4band)
plt.plot(_5n, _5band)
plt.plot(_6n, _6band)
plt.plot(_7n, _7band)
plt.plot(_8n, _8band)

plt.ylabel('Bandwidth in GBps')
plt.xlabel('Message size in MB')

plt.legend(['1/8 doubles',
            '2/8 doubles',
            '3/8 doubles',
            '4/8 doubles',
            '5/8 doubles',
            '6/8 doubles',
            '7/8 doubles',
            '8/8 doubles'])
plt.show()
