import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [2000, 4000, 8000, 16000, 32000]
y1 =[100, 180, 400, 812, 1589]
y2 =[80, 155, 325, 645, 1300]
y3 =[91, 186, 372, 768, 1501]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s', label='Domination')
ax1.plot(x, y2, 'r', label='Vector')
ax1.plot(x, y3, 'c', label='BM25')
ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,1800)
plt.legend(loc="lower right")

plt.savefig('wiki.eps',format='eps')
