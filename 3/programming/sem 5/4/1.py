import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",")

x = data[:,0]
y = data[:,2]

x = np.sort(x[~np.isnan(y)])
y = np.sort(y[~np.isnan(y)])


fxy1 = np.polyfit(x, y, 1, full=False)
f1 = np.poly1d(fxy1)
fx = np.linspace(0, x, 500) 

# plt.scatter(x, y, s=10)
plt.plot(x, y, linewidth=1.0,color='r')
# plt.plot(fx,f1(fx),linewidth=1.0,color='r')
plt.title('Стоймость квартиры от площади')
plt.xlabel("Площадь")
plt.ylabel("Стоймость")
# plt.xticks([w*7*24 for w in range(30)],["%i" % w for w in range(30)])
plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color='0.8')
print(f1([1650.3, 2200.4]))
plt.show()