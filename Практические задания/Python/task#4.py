import numpy as np
from numpy import matlib as mtlb
from matplotlib import pyplot as plt

# вычисление погрешностей мат ожидания и медианы по формуле:
def Formula(n, dn, medN):
    erMean = (1 / np.size(dn)) * sum(dn)
    dwnN = n - dn
    upN = n + dn
    dwnMed = np.median(dwnN)
    upMed = np.median(upN)
    erMed = max([medN - dwnMed, upMed - medN])
    return [erMean, erMed]

# вычисление погрешностей мат ожидания и медианы по методу Монте-Карло:
def MonteCarlo(n, dn, meanN, medN):
    m = pow(10, 3) # число повторов
    k = np.size(n)
    errors = np.zeros([k, m])
    for i in range(k):
        errors[i, :] = np.random.uniform(-dn[i], dn[i], m)
    tmN = mtlb.repmat(n, m, 1)
    inacN = np.transpose(tmN) + errors
    inacMean = np.zeros(m)
    inacMed = np.zeros(m)
    for i in range(m):
        inacMean[i] = np.mean(inacN[:, i])
        inacMed[i] = np.median(inacN[:, i])
    minErMean = abs(meanN - min(inacMean))
    maxErMean = abs(meanN - max(inacMean))
    erMean = max([minErMean, maxErMean])
    minErMed = abs(medN - min(inacMed))
    maxErMed = abs(medN - max(inacMed))
    erMed = max([minErMed, maxErMed])
    return [erMean, erMed]

m = range(10, 1010, 10) # количество чисел в выборке
k = np.size(m)
erFormula = np.zeros([2, k])
erMonteCarlo = np.zeros([2, k])
for i in range(k):
    n = np.random.uniform(-1, 1, m[i])
    dn = np.random.uniform(0.1, 0.2, m[i])
    meanN = np.mean(n)
    medN = np.median(n)
    [erFormula[0, i], erFormula[1, i]] = Formula(n, dn, medN)
    [erMonteCarlo[0, i], erMonteCarlo[1, i]] = MonteCarlo(n, dn, meanN, medN)
# мат ожидание:
# plt.plot(m, erFormula[0, :], m, erMonteCarlo[0, :])
# plt.xlabel("n")
# plt.ylabel("Error of Mean")
# plt.legend(["Formula", "Monte-Carlo"])
# plt.show()
# медиана:
plt.plot(m, erFormula[1, :], m, erMonteCarlo[1, :])
plt.xlabel("n")
plt.ylabel("Error of Med")
plt.legend(["Formula", "Monte-Carlo"])
plt.show()