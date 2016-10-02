import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'size': 15}
matplotlib.rc('font', **font)

width = 0.5 
p1=np.array([0.5,4])
p2=np.array([1,4.5])
p3=np.array([1.5,5])
p4=np.array([2,5.5])
p5=np.array([2.5,6])


r1=np.array([0.46,0.39])
r2=np.array([0.49,0.47])
r3=np.array([0.46,0.42])
r4=np.array([0.49,0.45])
r5=np.array([0.48,0.43])

fig, ax = plt.subplots()
rects1 = ax.bar(p1, r1, width, color='c',label='Optimal')

rects2 = ax.bar(p2, r2, width, color='y',label='HC99')

rects3 = ax.bar(p3, r3, width, color='r',label='HCWM')

rects4 = ax.bar(p4, r4, width, color='g',label='HAC')

rects5 = ax.bar(p5, r5, width, color='b',label='BiSeg')
ax.set_ylabel('Error (%)')
ax.set_xticks([0,1.8,5.2])
ax.set_ylim(0,1)
ax.set_xlim(0,7)
ax.set_xticklabels( ('','Wikipedia', 'Paper') )

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height),ha='center', va='bottom')

plt.legend(loc="upper right")
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)

plt.savefig('seg_pk.eps',format='eps')
