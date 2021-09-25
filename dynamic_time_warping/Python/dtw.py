# import numpy as np
# from sklearn.cluster import KMeans
# from scipy import signal
# import pandas as pd
#
# def dtw(setSign1, setSign2, p):
#     amnt = np.size(setSign1, axis=0)
#     lngth1 = np.size(setSign1, axis=1)
#     lngth2 = np.size(setSign2, axis=1)
#     m1 = np.zeros([amnt, lngth1, lngth2])
#     tmV = np.zeros([amnt, lngth2, lngth1])
#     for i in range(lngth2):
#         m1[:, :, i] = setSign1
#     for i in range(lngth1):
#         tmV[:, :, i] = setSign2
#     m2 = np.zeros([amnt, lngth1, lngth2])
#     for i in range(lngth2):
#         m2[:, i, :] = tmV[:, :, i]
#     if p > 0:
#         m = (sum((abs(m1 - m2)) ^ p, 1)) ^ (1 / p)
#     if p == -1:
#         m = max(abs(m1 - m2))
#     if p == -2:
#         wEvk = np.arange(1 / amnt, 1, 1 / amnt)
#         wEvk = wEvk[: : -1]
#         tmV = (abs(m1 - m2)) ^ 2
#         for i in range(lngth1):
#             m[:, :, i] = np.zeros([amnt, lngth2])
#         for i in range(lngth1):
#             for j in range(lngth2):
#                 number = np.argsort(tmV[:, j, i])
#                 for e in range(amnt):
#                     m[number[e], j, i] = tmV[number[e], j, i] * wEvk[number[e]]
#         m = np.sqrt(sum(m))
#     D = np.zeros([lngth1, lngth2])
#     for i in range(lngth2):
#         D[i, :] = m[:, :, i]
#     T = np.zeros([lngth1, lngth2])
#     T[0, 0] = D[0, 0]
#     for n in range(1, lngth1):
#         T[n, 0] = D[n, 0] + T[n - 1, 0]
#     for m in range(1, lngth2):
#         T[0, m] = D[0, m] + T[0, m - 1]
#     for n in range(1, lngth1):
#         for m in range(1, lngth2):
#             T[n, m] = D[n, m] + min([T[n - 1, m], T[n - 1, m - 1], T[n, m - 1]])
#     n = lngth1
#     m = lngth2
#     k = 1
#     e = 1
#     path = np.zeros([lngth1, 2])
#     path[0, :] = [lngth1, lngth2]
#     while n + m != 2:
#         if n - 1 == 0:
#             m = m - 1
#         elif(m - 1) == 0:
#             n = n - 1
#         else:
#             number = np.argmin([T[n - 1, m], T[n, m - 1], T[n - 1, m - 1]])
#             if number == 0:
#                 n = n - 1
#             elif number == 1:
#                 m = m - 1
#             elif number == 2:
#                 n = n - 1
#                 m = m - 1
#     k = k + 1
#     e = e + 1
#     path[e, :] = [n, m]
#     d = T[lngth1, lngth2] / k
#     return d
#
# def clustering(amnt, vect, p):
#     amntClust = 3
#     d = np.zeros([amnt, amnt])
#     for i in range(amnt):
#         for j in range(amnt):
#             d[i, j] = dtw(vect[:, :, i], vect[:, :, j], p)
#     kmns = KMeans(np.transpose(d), amntClust)
#     nClust = kmns.labels_
#     cClust = kmns.cluster_centers_
#     e = np.zeros([1, amntClust])
#     for i in range(amnt):
#         for j in range(amntClust):
#             if nClust[i] == j:
#                 e[j] = e[j] + 1
# #     dist1 = np.zeros([e[0], amnt])
# #     dist2 = np.zeros([e[1], amnt])
# #     dist3 = np.zeros([e[2], amnt])
# #     for i in range(amnt):
# #         if nClust[i] == 1:
# #             dist1(e(1),:) = d(i,:);
# #
# # for i = 1 : e(1)
# #     dist1(i, :) = (dist1(i, :) - cClust(1, :)) .^ 2;
# # end
# # for i = 1 : e(2)
# #     dist2(i, :) = (dist2(i, :) - cClust(2, :)) .^ 2;
# # end
# # for i = 1 : e(3)
# #     dist3(i, :) = (dist3(i, :) - cClust(3, :)) .^ 2;
# # end
# # tmV1 = sqrt(sum(dist1, 2));
# # tmV2 = sqrt(sum(dist2, 2));
# # tmV3 = sqrt(sum(dist3, 2));
# #
# # for i = 1 : amntClust
# #     switch i
# #         case 1
# #             sumDist(i) = sum(tmV1);
# #         case 2
# #             sumDist(i) = sum(tmV2);
# #         case 3
# #             sumDist(i) = sum(tmV3);
# #     end
# # end
# # rslt = sum(sumDist);
#
# def download(n):
#     fileNames = [['ce.txt', 'cp.txt', 'se.txt', 'ts1.txt', 'ts2.txt', 'ts3.txt', 'ts4.txt', 'vs1.txt'], # Samplimg rate = 1 Hz
#                  ['fs1.txt', 'fs2.txt'], # Samplimg rate = 10 Hz
#                  ['eps1.txt', 'ps1.txt', 'ps2.txt', 'ps3.txt', 'ps4.txt', 'ps5.txt', 'ps6.txt']] # Samplimg rate = 100 Hz
#     lngths = []
#     for i, _ in enumerate(fileNames):
#         lngths.append(len(fileNames[i]))
#     for i, valLen in enumerate(lngths):
#         allData = np.loadtxt(fileNames[i][0])
#         for j in range(valLen - 1):
#             tmData = np.loadtxt(fileNames[i][j + 1])
#             allData = np.append(allData, tmData, axis=0)
#         dim = tmData.shape
#         if i == 0:
#             dataSR1 = allData.reshape(valLen, dim[0], dim[1])
#         elif i == 1:
#             dataSR10 = allData.reshape(valLen, dim[0], dim[1])
#         elif i == 2:
#             dataSR100 = allData.reshape(valLen, dim[0], dim[1])
#     finalData = np.zeros([sum(lngths), dataSR1.shape[1], dataSR1.shape[2]])
#     finalData[0 : lngths[0], :, :] = dataSR1
#     for i in range(lngths[0], sum(lngths)):
#         for j in range(finalData.shape[1]):
#             if i < lngths[0] + lngths[1]:
#                 finalData[i, j, :] = signal.decimate(dataSR10[i - lngths[0], j, :], 10)
#             else:
#                 finalData[i, j, :] = signal.decimate(dataSR100[i - lngths[0] - lngths[1], j, :], 100)
#     vect = np.zeros([n, sum(lngths), finalData.shape[2]])
#     for i in range(n):
#         for j in range(sum(lngths)):
#             vect[i, j, :] = finalData[j, i, :]
#     vectForClsf = np.zeros([sum(lngths), finalData.shape[2]])
#     for i in range(sum(lngths)):
#         vectForClsf[i, :] = finalData[i, n + 1, :]
#     return [vect, vectForClsf]
#
# [vect, vectForClsf] = download(10)
# df = pd.DataFrame(vect[0, :, :])
# fileName = 'vect.xlsx'
# df.to_excel(fileName)
# df = pd.DataFrame(vectForClsf)
# fileName = 'vectForClsf.xlsx'
# df.to_excel(fileName)
import numpy as np
from sklearn.cluster import KMeans
from scipy import signal
from matplotlib import pyplot as plt
import pandas as pd

def download(amnt):
    fileNames = [['ce.txt', 'cp.txt', 'se.txt', 'ts1.txt', 'ts2.txt', 'ts3.txt', 'ts4.txt', 'vs1.txt'], # Samplimg rate = 1 Hz
                 ['fs1.txt', 'fs2.txt'], # Samplimg rate = 10 Hz
                 ['eps1.txt', 'ps1.txt', 'ps2.txt', 'ps3.txt', 'ps4.txt', 'ps5.txt', 'ps6.txt']] # Samplimg rate = 100 Hz
    lngths = []
    for i, _ in enumerate(fileNames):
        lngths.append(len(fileNames[i]))
    for i, valLen in enumerate(lngths):
        allData = np.loadtxt(fileNames[i][0])
        for j in range(valLen - 1):
            tmData = np.loadtxt(fileNames[i][j + 1])
            allData = np.append(allData, tmData, axis=0)
        dim = tmData.shape
        if i == 0:
            dataSR1 = allData.reshape(valLen, dim[0], dim[1])
        elif i == 1:
            dataSR10 = allData.reshape(valLen, dim[0], dim[1])
        elif i == 2:
            dataSR100 = allData.reshape(valLen, dim[0], dim[1])
    finalData = np.zeros([sum(lngths), dataSR1.shape[1], dataSR1.shape[2]])
    finalData[0 : lngths[0], :, :] = dataSR1
    for i in range(lngths[0], sum(lngths)):
        for j in range(finalData.shape[1]):
            if i < lngths[0] + lngths[1]:
                finalData[i, j, :] = signal.decimate(dataSR10[i - lngths[0], j, :], 10)
            else:
                finalData[i, j, :] = signal.decimate(dataSR100[i - lngths[0] - lngths[1], j, :], 100)
    vect = np.zeros([amnt, sum(lngths), finalData.shape[2]])
    for i in range(amnt):
        for j in range(sum(lngths)):
            vect[i, j, :] = finalData[j, i, :]
    vectForClsf = np.zeros([sum(lngths), finalData.shape[2]])
    for i in range(sum(lngths)):
        vectForClsf[i, :] = finalData[i, amnt + 1, :]
    return [vect, vectForClsf]

def dtw(setSign1, setSign2, p):
    amnt = np.size(setSign1, axis=0)
    lngth1 = np.size(setSign1, axis=1)
    lngth2 = np.size(setSign2, axis=1)
    m1 = np.zeros([lngth2, amnt, lngth1])
    tmV = np.zeros([lngth1, amnt, lngth2])
    for i in range(lngth2):
        m1[i, :, :] = setSign1
    for i in range(lngth1):
        tmV[i, :, :] = setSign2
    m2 = np.zeros([lngth2, amnt, lngth1])
    for i in range(lngth2):
        m2[:, :, i] = np.transpose(tmV[i, :, :])
    m = ((abs(m1 - m2)) ** p).sum(axis=1) ** (1 / p)
    if p == -1:
        m = max(abs(m1 - m2))
    if p == -2:
        wEvk = np.arange(1 / amnt, 1, 1 / amnt)
        wEvk = wEvk[: : -1]
        tmV = (abs(m1 - m2)) ** 2
        for i in range(lngth1):
            m[i, :, :] = np.zeros([amnt, lngth2])
        for i in range(lngth1):
            for j in range(lngth2):
                number = np.argsort(tmV[i, :, j])
                for e in range(amnt):
                    m[i, number[e], j] = tmV[i, number[e], j] * wEvk[number[e]]
        m = np.sqrt(m.sum(axis=1))
    D = m
    T = np.zeros([lngth1, lngth2])
    T[0, 0] = D[0, 0]
    for n in range(1, lngth1):
        T[n, 0] = D[n, 0] + T[n - 1, 0]
    for m in range(1, lngth2):
        T[0, m] = D[0, m] + T[0, m - 1]
    for n in range(1, lngth1):
        for m in range(1, lngth2):
            T[n, m] = D[n, m] + min([T[n - 1, m], T[n - 1, m - 1], T[n, m - 1]])
    n = lngth1
    m = lngth2
    k = 1
    path = [lngth1, lngth2]
    while n + m != 2:
        if n - 1 == 0:
            m = m - 1
        elif(m - 1) == 0:
            n = n - 1
        else:
            number = np.argmin([T[n - 2, m - 1], T[n - 1, m - 2], T[n - 2, m - 2]])
            if number == 0:
                n = n - 1
            elif number == 1:
                m = m - 1
            elif number == 2:
                n = n - 1
                m = m - 1
        path.append([n, m])
        k = k + 1
    d = T[lngth1 - 1, lngth2 - 1] / k
    return d

def clustering(amnt, vect, p):
    d = np.zeros([amnt, amnt])
    for i in range(amnt):
        for j in range(amnt):
            d[i, j] = dtw(vect[i, :, :], vect[j, :, :], p)
    kmns = KMeans(n_clusters=amntClust).fit(np.transpose(d))
    nClust = kmns.labels_
    cClust = kmns.cluster_centers_
    dCopy = d
    for i in range(amnt):
        for j in range(amntClust):
            if nClust[i] == j:
                dCopy[i, :] = (dCopy[i, :] - cClust[j, :]) ** 2
    dCopy = dCopy.sum(axis=1)
    sumDist = np.zeros(amntClust)
    for i in range(amnt):
        for j in range(amntClust):
            if nClust[i] == j:
                sumDist[j] = sumDist[j] + dCopy[i]
    sumDist = np.sqrt(sumDist)
    return [sum(sumDist), cClust]

amnt = 10
amntClust = 3
# [vect, vectForClsf] = download(amnt)
# np.save('vect.npy', vect)
# np.save('vectForClsf.npy', vectForClsf)
vect = np.load('vect.npy')
vectForClsf = np.load('vectForClsf.npy')
# p = [1, 1.5, 2, 3, 4, -1, -2]
# p = [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = np.arange(1, 20, 0.1)
result = np.zeros(len(p))
for i in range(len(p)):
    [sumDist, cClust] = clustering(amnt, vect, p[i])
    dVectClsf = np.zeros(amnt)
    for j in range(amnt):
        dVectClsf[j] = dtw(vectForClsf, vect[j, :, :], p[i])
    arrd = np.zeros(amntClust)
    for j in range(amntClust):
        arrd[j] = np.sqrt(sum((dVectClsf - cClust[j, :]) ** 2))
    result[i] = sumDist
plt.plot(p, result)
plt.xlabel("p")
plt.ylabel("sumDist")
plt.show()