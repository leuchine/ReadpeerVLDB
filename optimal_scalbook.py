import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [100,200,400,800,1600]
y1 =[3.66,5.96,9.95,21.26,43.41]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='DP, Query')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,50)

plt.legend(loc="upper right")

plt.savefig('optimal_scalbook.eps',format='eps')
