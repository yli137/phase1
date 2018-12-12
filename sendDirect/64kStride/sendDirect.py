import pandas as pd
import matplotlib.pyplot as plt

col = ['0','1','2','3','4','5','6','7','8','9','11','22']
r32 = pd.read_csv('../64kstride/r32.txt', sep=' ', names=col)
r512 = pd.read_csv('../64kstride/r512.txt', sep=' ', names=col)
r4k = pd.read_csv('../64kstride/r4k.txt', sep=' ', names=col)
r16k = pd.read_csv('../64kstride/r16k.txt', sep=' ', names=col)
r64k = pd.read_csv('../64kstride/r64k.txt', sep=' ', names=col)

r32s = r32.iloc[:, 1]
r512s = r512.iloc[:, 1]
r4ks = r4k.iloc[:, 1]
r16ks = r16k.iloc[:, 1]
r64ks = r64k.iloc[:, 1]

r32send = r32.iloc[:, 5]    ; r32put = r32.iloc[:, -3];
r512send = r512.iloc[:, 5]  ; r512put = r512.iloc[:, -3];
r4ksend = r4k.iloc[:, 5]    ; r4kput = r4k.iloc[:, -3];
r16ksend = r16k.iloc[:, 5]  ; r16kput = r16k.iloc[:, -3];
r64ksend = r64k.iloc[:, 5]  ; r64kput = r64k.iloc[:, -3];

r32sstd = r32.iloc[:, 7]     ; r32pstd = r32.iloc[:, -1];
r512sstd = r512.iloc[:, 7]   ; r512pstd = r512.iloc[:, -1];
r4ksstd = r4k.iloc[:, 7]     ; r4kpstd = r4k.iloc[:, -1];
r16ksstd = r16k.iloc[:, 7]   ; r16kpstd = r16k.iloc[:, -1];
r64ksstd = r64k.iloc[:, 7]   ; r64kpstd = r64k.iloc[:, -1];

f32 = plt.figure()
ax32 = f32.add_subplot(111)
plt.plot(r32s, r32send, color='red')
plt.plot(r32s, r32put, color='blue')
plt.errorbar(r32s, r32send, r32sstd, linestyle='None')
plt.errorbar(r32s, r32put, r32pstd, linestyle='None')
plt.ylabel("Time (s)")
plt.xlabel("blocklen (bytes)")
plt.ylim(0, .10)
plt.legend(['pack/unpack', 'put'])
plt.title('32 Byte/block, 64k stride')

f512 = plt.figure()
ax512 = f512.add_subplot(111)
plt.plot(r512s, r512send, color='red')
plt.plot(r512s, r512put, color='blue')
plt.errorbar(r512s, r512send, r512sstd, linestyle='None')
plt.errorbar(r512s, r512put, r512pstd, linestyle='None')
plt.ylim(0, 1.2)
plt.ylabel("Time (s)")
plt.xlabel("blocklen (bytes)")
plt.legend(['pack/unpack', 'put'])
plt.title('512 Byte/block, 64k stride')

f4k = plt.figure()
ax4k = f4k.add_subplot(111)
plt.plot(r4ks, r4ksend, color='red')
plt.plot(r4ks, r4kput, color='blue')
plt.errorbar(r4ks, r4ksend, r4ksstd, linestyle='None')
plt.errorbar(r4ks, r4kput, r4kpstd, linestyle='None')
plt.ylim(0, 6)
plt.ylabel("Time (s)")
plt.xlabel("blocklen (bytes)")
plt.legend(['pack/unpack', 'put'])
plt.title('4k Byte/block, 64k stride')

f16k = plt.figure()
ax16k = f16k.add_subplot(111)
plt.plot(r16ks, r16ksend, color='red')
plt.plot(r16ks, r16kput, color='blue')
plt.errorbar(r16ks, r16ksend, r16ksstd, linestyle='None')
plt.errorbar(r16ks, r16kput, r16kpstd, linestyle='None')
plt.ylim(0, 9)
plt.ylabel("Time (s)")
plt.xlabel("blocklen (bytes)")
plt.legend(['pack/unpack', 'put'])
plt.title('16k Byte/block, 64k stride')

f64k = plt.figure()
ax64k = f64k.add_subplot(111)
plt.plot(r64ks, r64ksend, color='red')
plt.plot(r64ks, r64kput, color='blue')
plt.errorbar(r64ks, r64ksend, r64ksstd, linestyle='None')
plt.errorbar(r64ks, r64kput, r64kpstd, linestyle='None')
plt.ylim(0, 12)
plt.ylabel("Time (s)")
plt.xlabel("blocklen (bytes)")
plt.legend(['pack/unpack', 'put'])
plt.title('64k Byte/block, 64k stride')

plt.show()
