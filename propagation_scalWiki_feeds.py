import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [0.1,1,10,100]
y1 =[50,501,4162,50118]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='TotalTime')

ax1.set_xlabel('Socail Feeds Size(K)')
ax1.set_ylabel('Time(ms)')

ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_ylim(10,1000000)
plt.legend(loc="upper right")

plt.savefig('propagation_scalWiki_feeds.eps',format='eps')
