import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [10,20,30,40,50]
y1 =[0.0039,0.01,0.018,0.036,0.07]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='DynamicTime')

ax1.set_xlabel('N')
ax1.set_ylabel('Time(ms)')

ax1.set_xticks([10,20,30,40,50])

plt.legend(loc="upper right")

plt.text(0.1, 0.95,'k=10', horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)

plt.savefig('sensiN_dynamic.eps',format='eps')
