import math
import numpy as np
from matplotlib import pyplot as plt

def Function(x1, x2, x3):
    return 3 * x1 + 4 * x2 * math.exp(x3)

x = np.array([1, 1, 0])
n = 300
dy1 = np.zeros(n)
dy2 = np.zeros(n)
d = np.zeros(n)
for i in range(n):
    d[i] = pow(10, - n + i)
    dy1[i] = (Function(x[0], x[1] + d[i], x[2]) - Function(x[0], x[1], x[2])) / d[i]
    spclD = 1j * d[i]
    dy2[i] = (Function(x[0], x[1] + spclD, x[2]) - Function(x[0], x[1], x[2])).imag / d[i]
plt.semilogx(d, dy1, d, dy2)
plt.title("Зависимость оценки производной")
plt.xlabel("d")
plt.ylabel("dy")
plt.legend(["Конечные разности", "Complex-step"])
plt.show()