import math
import numpy as np
from scipy.stats import t, norm, chi2
from matplotlib import pyplot as plt

def dataGeneration(m):
    genData = np.zeros([3, m])
    genData[0, :] = np.random.normal(0, 1, m)
    genData[1, :] = np.random.uniform(-math.sqrt(3), math.sqrt(3), m)
    genData[2, :] = np.random.exponential(1, m)
    return genData

def plotRes(n, arr, ttl):
    plt.plot(n, arr[:, 0], n, arr[:, 1], n, arr[:, 2])
    plt.title(ttl)
    plt.xlabel("The amount of numbers")
    plt.ylabel("Confidence interval")
    plt.legend(["norm", "unif", "exp"])
    plt.show()

def stIntMean(arr, P):
    mean = np.mean(arr)
    sd = np.std(arr)
    tSt = t.ppf(0.5 * (1 + P), np.size(arr) - 1)
    return [mean - (sd / math.sqrt(np.size(arr))) * tSt, mean + (sd / math.sqrt(np.size(arr))) * tSt]

def horaIntMean(arr, P):
    mean = np.mean(arr)
    minV = min(arr)
    maxV = max(arr)
    k = math.sqrt(-(math.log((1 - P) / 2) / (2 * np.size(arr)))) - 1 / (6 * np.size(arr))
    return [mean - (maxV - minV) * k, mean + (maxV - minV) * k]

def confIntMean(arr, P, m, iSt, iHora):
    [lSt, rSt] = stIntMean(arr, P)
    [lHora, rHora] = horaIntMean(arr, P)
    if ((m >= lSt) and (m <= rSt)):
        iSt += 1
    if ((m >= lHora) and (m <= rHora)):
        iHora += 1
    return [iSt, iHora]

def intForMean(n, P, r):
    l = np.size(n)
    resSt = np.zeros([l, 3])
    resHora = np.zeros([l, 3])
    for i in range(l):
        for j in range(r):
            data = dataGeneration(n[i])
            [resSt[i, 0], resHora[i, 0]] = confIntMean(data[0, :], P, 0, resSt[i, 0], resHora[i, 0])
            [resSt[i, 1], resHora[i, 1]] = confIntMean(data[1, :], P, 0, resSt[i, 1], resHora[i, 1])
            [resSt[i, 2], resHora[i, 2]] = confIntMean(data[2, :], P, 1, resSt[i, 2], resHora[i, 2])
        resSt[i, :] /= r
        resHora[i, :] /= r
    plotRes(n, resSt, "Mean (Student)")

def confIntMed(arr, P, m, count):
    koefN = norm.ppf(0.5 * (1 + P), 0, 1)
    amount = np.size(arr)
    l = math.floor(amount / 2 - 0.5 * math.sqrt(amount) * koefN)
    r = math.ceil(amount / 2 + 0.5 * math.sqrt(amount) * koefN)
    if ((m >= arr[l]) and (m <= arr[r])):
        count += 1
    return count

def intForMed(n, P, r):
    l = np.size(n)
    res = np.zeros([l, 3])
    for i in range(l):
        for j in range(r):
            data = dataGeneration(n[i])
            res[i, 0] = confIntMed(data[0, :], P, 0, res[i, 0])
            res[i, 1] = confIntMed(data[1, :], P, 0, res[i, 1])
            res[i, 2] = confIntMed(data[2, :], P, 1, res[i, 2])
        res[i, :] /= r
    plotRes(n, res, "Median")

def confIntDisp(arr, P, d, count):
    amount = np.size(arr)
    koef1 = chi2.ppf(0.5 * (1 + P), amount - 1)
    koef2 = chi2.ppf(0.5 * (1 - P), amount - 1)
    l = (np.var(arr) * (amount - 1)) / koef1
    r = (np.var(arr) * (amount - 1)) / koef2
    if ((d >= l) and (d <= r)):
        count += 1
    return count

def intForDisp(n, P, r):
    l = np.size(n)
    res = np.zeros([l, 3])
    for i in range(l):
        for j in range(r):
            data = dataGeneration(n[i])
            res[i, 0] = confIntDisp(data[0, :], P, 1, res[i, 0])
            res[i, 1] = confIntDisp(data[1, :], P, 1, res[i, 1])
            res[i, 2] = confIntDisp(data[2, :], P, 1, res[i, 2])
        res[i, :] /= r
    plotRes(n, res, "Disp")

n = range(100, 2000, 100)
P = 0.95
r = 1000
prmtr = 3
if (prmtr == 1):
    intForMean(n, P, r)
elif (prmtr == 2):
    intForMed(n, P, r)
elif (prmtr == 3):
    intForDisp(n, P, r)