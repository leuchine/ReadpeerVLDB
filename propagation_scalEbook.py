import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [100,200,400,800,1600]
y1 =[50,103,235,480,890]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='Ranking')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,900)

plt.legend(loc="upper right")

plt.savefig('propagation_scalEbook.eps',format='eps')
