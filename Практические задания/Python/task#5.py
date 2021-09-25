import numpy as np
from numpy import matlib as mtlb
from matplotlib import pyplot as plt
import math

# вычисление MAD:
def MAD(n):
    return np.median(n - np.median(n))

# вычисление погрешностей СКО и MAD по формуле:
def Formula(n, dn, sdN):
    meanN = np.mean(n)
    erD = (2/ (np.size(n) - 1)) * sum((n - meanN) * dn)
    erSD = max([sdN - math.sqrt(pow(sdN, 2) - erD), math.sqrt(pow(sdN, 2) + erD) - sdN])
    dwnN = n - dn
    upN = n + dn
    dwnMed = np.median(dwnN)
    upMed = np.median(upN)
    erMed = max([np.median(n) - dwnMed, upMed - np.median(n)])
    erMAD = np.median(dn + erMed)
    return [erSD, erMAD]

# вычисление погрешностей СКО и MAD по методу Монте-Карло:
def MonteCarlo(n, dn, sdN, madN):
    m = pow(10, 3) # число повторов
    k = np.size(n)
    errors = np.zeros([k, m])
    for i in range(k):
        errors[i, :] = np.random.uniform(-dn[i], dn[i], m)
    tmN = mtlb.repmat(n, m, 1)
    inacN = np.transpose(tmN) + errors
    inacSD = np.zeros(m)
    inacMAD = np.zeros(m)
    for i in range(m):
        inacSD[i] = np.std(inacN[:, i])
        inacMAD[i] = MAD(inacN[:, i])
    minErSD = abs(sdN - min(inacSD))
    maxErSD = abs(sdN - max(inacSD))
    erSD = max([minErSD, maxErSD])
    minErMAD = abs(madN - min(inacMAD))
    maxErMAD = abs(madN - max(inacMAD))
    erMAD = max([minErMAD, maxErMAD])
    return [erSD, erMAD]

m = range(10, 1010, 10) # количество чисел в выборке
k = np.size(m)
erFormula = np.zeros([2, k])
erMonteCarlo = np.zeros([2, k])
for i in range(k):
    n = np.random.uniform(-1, 1, m[i])
    dn = np.random.uniform(0.1, 0.2, m[i])
    sdN = np.std(n)
    madN = MAD(n)
    [erFormula[0, i], erFormula[1, i]] = Formula(n, dn, sdN)
    [erMonteCarlo[0, i], erMonteCarlo[1, i]] = MonteCarlo(n, dn, sdN, madN)
# # СКО:
# plt.plot(m, erFormula[0, :], m, erMonteCarlo[0, :])
# plt.xlabel("n")
# plt.ylabel("Error of SD")
# plt.legend(["Formula", "Monte-Carlo"])
# plt.show()
# MAD:
plt.plot(m, erFormula[1, :], m, erMonteCarlo[1, :])
plt.xlabel("n")
plt.ylabel("Error of MAD")
plt.legend(["Formula", "Monte-Carlo"])
plt.show()