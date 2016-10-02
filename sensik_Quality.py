import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [5,10,15,20,25]
y1 =[43.45,43.3,43.36,43.6,43.5]
fig, ax1 = plt.subplots()

ax1.plot(x, y1, 'g-s',label='QualityTime')

ax1.set_xlabel('k')
ax1.set_ylabel('Time(ms)')

ax1.set_xticks(x)
ax1.set_ylim([0,60])
plt.legend(loc="upper right")

plt.text(0.1, 0.95,'N=30', horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)

plt.savefig('sensiK_quality.eps',format='eps')
