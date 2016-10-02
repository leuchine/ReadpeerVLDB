import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [10,20,30,40,50]
y1 =[0.0095,0.0175,0.025,0.031,0.036]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='DynamicTime')

ax1.set_xlabel('k')
ax1.set_ylabel('Time(ms)')
ax1.set_ylim([0, 0.045])
ax1.set_xticks([10,20,30,40,50])

plt.legend(loc="upper right")

plt.text(0.1, 0.95,'N=30', horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)

plt.savefig('sensiK_dynamic.eps',format='eps')
