import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [5,10,15,20,25]
y1 =[43.4,43.35,43.39,43.64,43.35]
y2 =[14.2,9.42,5.82,2.88,0.09]
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-s',label='TotalTime')
ax2.plot(x[0],y1[0],'g-s',label='TotalTime')
ax2.plot(x, y2, 'b-o',label='Max-Quality')

ax1.set_xlabel('k')
ax1.set_ylabel('Time(ms)')
ax1.set_ylim([0, 70])
ax2.set_ylabel('Quality')
ax2.set_ylim([0, 15])
ax1.set_xticks(x)

plt.legend(loc="upper right")

plt.text(0.1, 0.95,'N=30',horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)

plt.savefig("sensiK.eps",format='eps')
