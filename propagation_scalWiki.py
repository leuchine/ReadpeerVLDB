import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [2000,4000,8000,16000,32000]
y1 =[1.2, 2.6,4.2,8.1,16]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='Ranking')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(1000 sec)')

ax1.set_ylim(0,15)

plt.legend(loc="upper right")

plt.savefig('propagation_scalWiki.eps',format='eps')
