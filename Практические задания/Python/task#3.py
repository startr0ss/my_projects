import cmath
import math
import numpy as np
from numpy import matlib as mtlb
from matplotlib import pyplot as plt

def Function1(x1, x2, x3, x4):
    return cmath.sqrt(x1 ** 2 + x2 ** 2 + x3 ** 2) + cmath.atan(x4 / (x1 + x2 + x3 + x4))

def Function2(x1, x2, x3, x4):
    return math.sqrt(x1 ** 2 + x2 ** 2 + x3 ** 2) + math.atan(x4 / (x1 + x2 + x3 + x4))

def ComplexStep(x, delta, deltaX1):
    deltaY = np.zeros(np.size(deltaX1))
    alpha = pow(10, -100)
    d = 1j * alpha
    df1 = abs((Function1(x[0] + d, x[1], x[2], x[3])).imag / alpha)
    df2 = abs((Function1(x[0], x[1] + d, x[2], x[3])).imag / alpha)
    df3 = abs((Function1(x[0], x[1], x[2] + d, x[3])).imag / alpha)
    df4 = abs((Function1(x[0], x[1], x[2], x[3] + d)).imag / alpha)
    for i in range(np.size(deltaX1)):
        deltaY[i] = df1 * deltaX1[i] + df2 * delta[0] + df3 * delta[1] + df4 * delta[2]
    return deltaY


def MonteCarlo(x, delta, deltaX1):
    deltaY = np.zeros(np.size(deltaX1))
    m = 1000
    y0 = Function2(x[0], x[1], x[2], x[3])
    for i in range(np.size(deltaX1)):
        errors = np.zeros([np.size(x), m])
        for j in range(np.size(x)):
            if j == 0:
                errors[j, :] = np.random.uniform(-deltaX1[i], deltaX1[i], m)
            else:
                errors[j, :] = np.random.uniform(-delta[j - 1], delta[j - 1], m)
        y = np.zeros(m)
        for j in range(m):
            tmX = x + np.transpose(errors[:, j])
            y[j] = Function2(tmX[0], tmX[1], tmX[2], tmX[3])
        min_dy = abs(y0 - min(y))
        max_dy = abs(y0 - max(y))
        deltaY[i] = max([min_dy, max_dy])
    return deltaY

def ForKreinovich(v, dy):
    s = 0
    for i in range(np.size(dy)):
        s = s + (pow(v, 2) / (pow(v, 2) + pow(dy[i], 2)))
    return s - (np.size(dy) / 2)

def Kreinovich(x, delta, deltaX1):
    deltaY = np.zeros(np.size(deltaX1))
    m = 300
    coef = 1
    y0 = Function2(x[0], x[1], x[2], x[3])
    for i in range(np.size(deltaX1)):
        tmX = mtlb.repmat(x, m, 1)
        tmX = np.transpose(tmX)
        r = np.random.uniform(0, 1, [np.size(x), m])
        for j in range(np.size(x)):
            for e in range(m):
                if j == 0:
                    tmX[j, e] = tmX[j, e] + coef * deltaX1[i] * math.tan(math.pi * (r[j, e] - 0.5))
                else:
                    tmX[j, e] = tmX[j, e] + coef * delta[j - 1] * math.tan(math.pi * (r[j, e] - 0.5))
        dy = np.zeros(m)
        for j in range(m):
            dy[j] = Function2(tmX[0, j], tmX[1, j], tmX[2, j], tmX[3, j]) - y0
        minV = 0
        maxV = max(dy)
        length = maxV - minV
        while length > pow(10, -4):
            if ForKreinovich(minV, dy) * ForKreinovich(maxV, dy) < 0:
                c = (minV + maxV) / 2
                if ForKreinovich(minV, dy) * ForKreinovich(c, dy) < 0:
                    maxV = c
                else:
                    minV = c
            length = maxV - minV
        deltaY[i] = (maxV + minV) / 2
    return deltaY

k = 4
x = np.array([1, 0.73, 2.54, 10.3])
delta = np.array([0.01, 0.05, 0.1])
deltaX1 = np.arange(0, 0.2, 0.01)
deltaY1 = ComplexStep(x, delta, deltaX1)
deltaY2 = MonteCarlo(x, delta, deltaX1)
deltaY3 = Kreinovich(x, delta, deltaX1)
plt.plot(deltaX1, deltaY1, deltaX1, deltaY2, deltaX1, deltaY3)
plt.xlabel("deltaX1")
plt.ylabel("deltaY")
plt.legend(["Complex-step", "Monte-Carlo", "Kreinovich"])
plt.show()