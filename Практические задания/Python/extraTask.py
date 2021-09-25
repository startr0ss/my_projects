import numpy as np
from numpy import matlib as mtlb
from scipy.stats import f, norm
import math
from matplotlib import pyplot as plt

def funct(a, b, x):
    return a * (x ** 2) + b * x

n = 100
r = 10
baseA = 1
baseB = -1
baseX = np.arange(0, 3, 3 / n)
baseY = np.zeros(n)
baseY = funct(baseA, baseB, baseX)
y1 = mtlb.repmat(baseY, r, 1)
for i in range(r):
    y1[i, :] = baseY + np.random.normal(0, 0.1, n)
m = 200
a = np.arange(-3, 3, 6 / m)
b = np.arange(-3, 3, 6 / m)
y2 = np.zeros([m ** 2, n])
for i in range(m):
    for j in range(m):
        y2[i * m + j, :] = funct(a[i], b[i], baseX)
# классический критерий
meanY1_1 = mtlb.repmat(np.mean(y1, 0), r, 1)
sY1 = (1 / (r - 1)) * np.sum((y1 - meanY1_1) ** 2, axis=0)
sVospr = (1 / n) * np.sum(sY1)
meanY1_2 = mtlb.repmat(np.mean(y1, 0), m ** 2, 1)
sAdek = (2 / (n - r)) * np.sum(((y2 - meanY1_2) ** 2), axis=1)
koef = sAdek / sVospr
alpha = 0.05
border1 = f.ppf(1 - alpha, n - 2, n * (r - 1))
count1 = 0
a1 = np.zeros(m)
b1 = np.zeros(m)
for i in range(m ** 2):
    if koef[i] < border1:
        a1[count1] = a[math.floor((i - 1) / m) + 1]
        b1[count1] = b[((i - 1) % m) + 1]
        count1 = count1 + 1
# критерий Вальда-Вольфовица
allR = meanY1_2 - y2
count2 = 0
a2 = np.zeros(m * 3)
b2 = np.zeros(m * 3)
for i in range(m ** 2):
    r = allR[i, :]
    ind = 1
    nSer = 1
    nPos = 0
    nOtr = 0
    while ind < n:
        if r[ind] * r[ind - 1] < 0:
            nSer += 1
        if r[ind - 1] > 0:
            nPos += 1
        ind += 1
    nOtr = n - nPos
    es = ((2 * nPos * nOtr) / (nPos + nOtr)) + 1
    ds = ((2 * nPos * nOtr) / ((nPos + nOtr) ** 2)) * (((2 * nPos * nOtr) - (nPos + nOtr)) / (nPos + nOtr - 1))
    v = (nSer - es) / math.sqrt(ds)
    border2 = norm.ppf(1 - alpha / 2, 0, 1)
    if abs(v) < border2:
        tmp = math.trunc(i / m) + 1
        a2[count2] = a[math.floor((i - 1) / m) + 1]
        b2[count2] = b[((i - 1) % m) + 1]
        count2 = count2 + 1
plt.plot(a1, b1, 'b.', a2, b2, 'r.')
plt.xlabel("a")
plt.ylabel("b")
plt.legend(["Classic", "VV"])
plt.show()