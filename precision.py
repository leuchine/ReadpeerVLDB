import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [60,100,140,180,220,260,300]
y1 =[0.75,0.79,0.86,0.95,0.98,1,1]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s')

ax1.set_xlabel('Length')
ax1.set_ylabel('Precision')

ax1.set_ylim(0,1)

plt.legend(loc="upper right")

plt.savefig('precision.eps',format='eps')
