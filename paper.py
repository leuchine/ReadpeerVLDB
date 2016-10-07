import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [100, 200, 400, 800, 1600]
y1 =[5, 8, 18, 35, 65]
y2 =[3.1, 5.4, 11.2, 22.8, 47]
y3 =[3.6, 7.4, 14.2, 27.8, 56.0]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s',label='Domination')
ax1.plot(x, y2, 'r', label='Vector')
ax1.plot(x, y3, 'c', label='BM25')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,70)
plt.legend(loc="lower right")

plt.savefig('paper.eps',format='eps')
