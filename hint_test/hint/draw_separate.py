import pandas as pd
import matplotlib.pyplot as plt

col=['1','2','3','4']
_1hint = pd.read_csv("1hintT0.txt", names=col, sep=' ')
_2hint = pd.read_csv("2hintT0.txt", names=col, sep=' ')
_3hint = pd.read_csv("3hintT0.txt", names=col, sep=' ')
_4hint = pd.read_csv("4hintT0.txt", names=col, sep=' ')
_5hint = pd.read_csv("5hintT0.txt", names=col, sep=' ')
_6hint = pd.read_csv("6hintT0.txt", names=col, sep=' ')
_7hint = pd.read_csv("7hintT0.txt", names=col, sep=' ')
_8hint = pd.read_csv("8hintT0.txt", names=col, sep=' ')

_1nohint = pd.read_csv("../nohint/1nohintT0.txt", names=col, sep=' ')
_2nohint = pd.read_csv("../nohint/2nohintT0.txt", names=col, sep=' ')
_3nohint = pd.read_csv("../nohint/3nohintT0.txt", names=col, sep=' ')
_4nohint = pd.read_csv("../nohint/4nohintT0.txt", names=col, sep=' ')
_5nohint = pd.read_csv("../nohint/5nohintT0.txt", names=col, sep=' ')
_6nohint = pd.read_csv("../nohint/6nohintT0.txt", names=col, sep=' ')
_7nohint = pd.read_csv("../nohint/7nohintT0.txt", names=col, sep=' ')
_8nohint = pd.read_csv("../nohint/8nohintT0.txt", names=col, sep=' ')

size = _1hint.iloc[:, 0]

_1hintspeed = _1hint.iloc[:, -2]
_2hintspeed = _2hint.iloc[:, -2]
_3hintspeed = _3hint.iloc[:, -2]
_4hintspeed = _4hint.iloc[:, -2]
_5hintspeed = _5hint.iloc[:, -2]
_6hintspeed = _6hint.iloc[:, -2]
_7hintspeed = _7hint.iloc[:, -2]
_8hintspeed = _8hint.iloc[:, -2]

_1nohintspeed = _1nohint.iloc[:, -2]
_2nohintspeed = _2nohint.iloc[:, -2]
_3nohintspeed = _3nohint.iloc[:, -2]
_4nohintspeed = _4nohint.iloc[:, -2]
_5nohintspeed = _5nohint.iloc[:, -2]
_6nohintspeed = _6nohint.iloc[:, -2]
_7nohintspeed = _7nohint.iloc[:, -2]
_8nohintspeed = _8nohint.iloc[:, -2]

fig, ax = plt.subplots(2, 4)
ax[0, 0].plot(size, _1hintspeed, label='hint', color='b')
ax[0, 1].plot(size, _1hintspeed, label='hint', color='b')
ax[0, 2].plot(size, _1hintspeed, label='hint', color='b')
ax[0, 3].plot(size, _1hintspeed, label='hint', color='b')
ax[1, 0].plot(size, _1hintspeed, label='hint', color='b')
ax[1, 1].plot(size, _1hintspeed, label='hint', color='b')
ax[1, 2].plot(size, _1hintspeed, label='hint', color='b')
ax[1, 3].plot(size, _1hintspeed, label='hint', color='b')

ax[0, 0].plot(size, _1nohintspeed, label="w/o hint", color='r')
ax[0, 1].plot(size, _1nohintspeed, label="w/o hint", color='r')
ax[0, 2].plot(size, _1nohintspeed, label="w/o hint", color='r')
ax[0, 3].plot(size, _1nohintspeed, label="w/o hint", color='r')
ax[1, 0].plot(size, _1nohintspeed, color='r')
ax[1, 1].plot(size, _1nohintspeed, color='r')
ax[1, 2].plot(size, _1nohintspeed, color='r')
ax[1, 3].plot(size, _1nohintspeed, color='r')

plt.show()
