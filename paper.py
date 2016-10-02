import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [100, 200, 400, 800, 1600]
y1 =[5, 8, 18, 35, 65]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,70)
plt.legend(loc="upper right")

plt.savefig('paper.eps',format='eps')
