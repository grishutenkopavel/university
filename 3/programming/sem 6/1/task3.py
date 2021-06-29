import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",")
square = data[:,0]
rooms = data[:,1]
cost = data[:,2]

# Удаляем nan
square = square[~np.isnan(square)]
rooms = rooms[~np.isnan(rooms)]
cost = cost[~np.isnan(cost)]
# print(square, rooms, cost)

# Среднее значение
avgSquare = np.mean(square)
avgRooms = np.mean(rooms)
avrCost = np.mean(cost)
# print(avr_square, avr_rooms, avr_cost)

# Диспресия
varSquare = np.var(square)
varRooms = np.var(rooms)
varCost = np.var(cost)
# print(var_square, var_rooms, var_cost)

# Среднеквадратичное отклонение
stdSquare = np.std(square)
stdRooms = np.std(rooms)
stdCost = np.std(cost)
# print(std_square, std_rooms, std_cost)

f1p = np.polyfit(square, cost, 1, full=False)
f1 = np.poly1d(f1p)
fx = np.linspace(0, square, 500)

plt.scatter(square, cost, s=10)
plt.plot(fx,f1(fx),linewidth=1.0,color='r')
plt.title('Цена квартиры от площади')
plt.xlabel("Площадь")
plt.ylabel("Стоймость")
plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color='0.75')
# Прогнозирование
print(f1([1650.3]))
plt.show()

