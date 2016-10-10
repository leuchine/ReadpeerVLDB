import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [60,100,140,180,220,260,300]
y1 =[1,1,1,1,1,1,1]
y2 =[0.42,0.5,0.49,0.64,0.68,0.70,0.73]
y3 =[0.45,0.56,0.63,0.65,0.73,0.74,0.80]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s', label='Domination')
ax1.plot(x, y2, 'r', label='Vector')
ax1.plot(x, y3, 'c', label='BM25')

ax1.set_xlabel('Length')
ax1.set_ylabel('Recall')

ax1.set_ylim(0,1.03)

plt.legend(loc="lower right")

plt.savefig('recall.eps',format='eps')
