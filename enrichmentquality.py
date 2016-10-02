import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'size': 16}
matplotlib.rc('font', **font)

width = 0.5 
p1=np.array([0.5,3])
p2=np.array([1,3.5])
p3=np.array([1.5,4])

r1=np.array([0.72,0.75])
r2=np.array([0.74,0.69])
r3=np.array([0.61,0.64])

fig, ax = plt.subplots()
rects1 = ax.bar(p1, r1, width, color='c',label='Reuters')

rects2 = ax.bar(p2, r2, width, color='y',label='Wikipedia')

rects3 = ax.bar(p3, r3, width, color='r',label='Paper')
ax.set_ylabel('MAP')
ax.set_xticks([0,1.3,3.8])
ax.set_ylim(0,1.19)
ax.set_xlim(0,5)
ax.set_xticklabels( ('','Crowdsourcing', 'User Study') )

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height),ha='center', va='bottom')

plt.legend(loc="upper right")
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.savefig('enrichmentquality.eps',format='eps')
