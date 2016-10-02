import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [10,20,30,40,50]
y1 =[4.74,19.1,43.33,77.6,132.4]
fig, ax1 = plt.subplots()

ax1.plot(x, y1, 'g-s',label='QualityTime')

ax1.set_xlabel('N')
ax1.set_ylabel('Time(ms)')

ax1.set_xticks(x)
ax1.set_ylim([0,160])
plt.legend(loc="upper right")

plt.text(0.1, 0.95,'k=10', horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)

plt.savefig('sensiN_quality.eps',format='eps')
