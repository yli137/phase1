import pandas as pd
import matplotlib.pyplot as plt

def resize_to_gb(x):
    return [p / 1000 for p in x]
fmemcpy = pd.read_csv("memcpy_test.txt", sep=' ')
fman = pd.read_csv("manualcpy_test.txt", sep=' ')
fmanpref = pd.read_csv("manualcpy_wprefetch.txt", sep=' ')

fmemcpyo3 = pd.read_csv("../memop_o3/memcpy_testO3.txt", sep=' ')
fmano3 = pd.read_csv("../memop_o3/manualcpy_testO3.txt", sep=' ')
fmanprefo3 = pd.read_csv("../memop_o3/manualcpy_wprefetchO3.txt", sep=' ')

bytes_ = fmemcpy.iloc[:, 2]
bytes_ = [x * 8 / 1000000 for x in bytes_]

memcpy = fmemcpy.iloc[:, -2]
memcpy = resize_to_gb(memcpy)
man = fman.iloc[:, -2]
man = resize_to_gb(man)
manpref = fmanpref.iloc[:, -2]
manpref = resize_to_gb(manpref)

memcpyo3 = fmemcpyo3.iloc[:, -2]
memcpyo3 = resize_to_gb(memcpyo3)
mano3 = fmano3.iloc[:, -2]
mano3 = resize_to_gb(mano3)
manprefo3 = fmanprefo3.iloc[:, -2]
manprefo3 = resize_to_gb(manprefo3)

plt.plot(bytes_, memcpy)
plt.plot(bytes_, man)
plt.plot(bytes_, manpref)
plt.plot(bytes_, memcpyo3)
plt.plot(bytes_, mano3)
plt.plot(bytes_, manprefo3)

plt.legend(["memcpy", "manual copy", "manual copy with prefetch",
            "memcpy with -O3", "manual copy with -O3",
            "manual copy with prefetch and -O3"], loc="upper right")
plt.xlabel("size (MB)")
plt.ylabel("bandwidth (GB/s)")
plt.title("Bandwidth vs. size")
plt.show()
