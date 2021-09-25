import numpy as np
from scipy.stats import f

sd = np.arange(0, 10, 0.1)
n1 = 4
n2 = 4
amount = 1000
p = 0.95
e = 0
arrayP = -1 * np.ones(np.size(sd))
result = []
for i in range(np.size(sd)):
    noSign = 0
    for j in range(amount):
        y = [[0.73, 1.24, 1.54, 1.90],
             [0.75, 1.27, 1.50, 1.74],
             [0.75, 1.35, 1.43, 1.92],
             [0.74, 1.20, 1.60, 1.79]]
        y = y + np.random.normal(0, sd[i], [n1, n2])
        means = np.mean(y, axis=0)
        s = np.var(y, axis=0)
        sV = (1 / n1) * sum(s)
        sT = np.var(means)
        k = (n2 * sT) / sV
        alpha = 0.01
        border = f.ppf(1 - alpha, n1 - 1, n1 * (n2 - 1))
        if k < border:
            noSign += 1
    arrayP[e] = noSign / amount
    e += 1
    if noSign / amount >= p:
        result.append(sd[i])
print(result)