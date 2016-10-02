import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [100,200,400,800,1600]
y1 =[0.366,0.596,0.995,2.126,4.341]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='DP, Query')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,5)

plt.legend(loc="upper right")

plt.savefig('optimal_scalbook.eps',format='eps')
