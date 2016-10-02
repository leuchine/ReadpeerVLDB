import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [10,20,30,40,50]
y1 =[4.74,19.1,43.3,77.6,122.4]
y2 =[15.01,10.4,6.7,3.5,0.5]
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-s',label='TotalTime')
ax2.plot(x[0],y1[0],'g-s',label='TotalTime')
ax2.plot(x, y2, 'b-o',label='Max-Quality')

ax1.set_xlabel('N')
ax1.set_ylabel('Time(ms)')
ax2.set_ylabel('Quality')
ax1.set_ylim([0, 170])
ax1.set_xticks([10,20,30,40,50])

plt.legend(loc="upper right")

plt.text(0.1, 0.95,'k=10', horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)

plt.savefig('sensiN.eps',format='eps')
