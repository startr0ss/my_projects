import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

data = np.load('dataWithErrors.npy') # load data with errors
M = 10 # the number of repeats
# kmeans clustering:
nCl = 0 # the number of clusters - 1
numbClFound = 0
sumDist = []
while numbClFound == 0:
    curSumDist = np.zeros(M)
    for i in range(M):
        kmns = KMeans(n_clusters=nCl + 1).fit(np.transpose(data[i][:][:]))
        curSumDist[i] = kmns.inertia_
    I1 = [min(curSumDist), max(curSumDist)]
    I2 = [np.mean(curSumDist) - 2 * np.std(curSumDist), np.mean(curSumDist) + 2 * np.std(curSumDist)]
    curSumDist = np.sort(curSumDist)
    I3 = [curSumDist[int(np.floor(0.025 * M))], curSumDist[int(np.ceil(0.975 * M)) - 1]]
    sumDist.append([nCl + 1, *I1, *I2, *I3])
    print(sumDist[nCl])
    if (nCl > 0) and (sumDist[nCl - 1][1] < sumDist[nCl][2]) and (sumDist[nCl - 1][3] < sumDist[nCl][4]) and (sumDist[nCl - 1][5] < sumDist[nCl][6]):
        numbClFound = 1
    nCl += 1
columnName = ["The amount of clusters", "I1[N^2]", "I1[N^2]", "I2[N^2]", "I2[N^2]", "I3[N^2]", "I3[N^2]"]
df = pd.DataFrame(sumDist)
fileName = 'sumDist.xlsx'
df.to_excel(fileName, header=columnName, index=False)