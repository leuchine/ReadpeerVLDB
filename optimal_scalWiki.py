import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [2000,4000,8000,16000,32000]
y1 =[89.4,176.6,348.8,703.1,1400]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='DP, Query')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,1800)

plt.legend(loc="upper right")

plt.savefig('optimal_scalWiki.eps',format='eps')
