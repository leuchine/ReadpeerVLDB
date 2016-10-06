import matplotlib.pyplot as plt
import matplotlib

font = {'size': 18}
matplotlib.rc('font', **font)

x = [100, 200, 400, 800, 1600]
y1 =[6, 10, 21, 37, 67]
fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'g-s', label='indexing')

ax1.set_xlabel('Size')
ax1.set_ylabel('Time(sec)')

ax1.set_ylim(0,75)
plt.legend(loc="upper right")

plt.savefig('paperindex.eps',format='eps')
