import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [2000, 4000, 8000, 16000, 32000]
y1 =[100, 180, 400, 812, 1589]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s', label='Domination')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,1800)
plt.legend(loc="upper right")

plt.savefig('wiki.eps',format='eps')
