import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",")
square = data[:,0]
rooms = data[:,1]
cost = data[:,2]

# Удаление nan
square = square[~np.isnan(square)]
rooms = rooms[~np.isnan(rooms)]
cost = cost[~np.isnan(cost)]
print(square, rooms, cost)

# Среднее значение
avgSquare = np.mean(square)
avgRooms = np.mean(rooms)
avgCost = np.mean(cost)
print(avgSquare, avgRooms, avgCost)

# Диспресия
varSquare = np.var(square)
varRooms = np.var(rooms)
varCost = np.var(cost)
print(varSquare, varRooms, varCost)

# Среднеквадратичное отклонение
stdSquare = np.std(square)
stdRooms = np.std(rooms)
stdCost = np.std(cost)
print(stdSquare, stdRooms, stdCost)


