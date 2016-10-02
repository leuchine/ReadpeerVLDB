import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [125,490,700,1400,2600]
y1 =[4.3,21,36,59,120]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='QualityTime')

ax1.set_xlabel('M')
ax1.set_ylabel('Time(ms)')
ax1.set_ylim([0, 160])
ax1.set_xticks([0,500,1000,1500,2000,2500,3000])

plt.legend(loc="upper right")

plt.text(0.14, 0.95,'N=30,k=10', horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)

plt.savefig('sensiM_quality.eps',format='eps')
