import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [60,100,140,180,220,260,300]
y1 =[0.75,0.79,0.86,0.95,0.98,1,1]
y2 =[0.45,0.52,0.60,0.66,0.70,0.72,0.76]
y3 =[0.49,0.54,0.65,0.68,0.73,0.77,0.81]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s', label='Domination')
ax1.plot(x, y2, 'r', label='Vector')
ax1.plot(x, y3, 'c', label='BM25')

ax1.set_xlabel('Length')
ax1.set_ylabel('Precision')

ax1.set_ylim(0,1)

plt.legend(loc="lower right")

plt.savefig('precision.eps',format='eps')
