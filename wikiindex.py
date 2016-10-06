import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [2000, 4000, 8000, 16000, 32000]
y1 =[112, 199, 410, 832, 1600]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s', label='indexing')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,1800)
plt.legend(loc="upper right")

plt.savefig('wikiindex.eps',format='eps')
