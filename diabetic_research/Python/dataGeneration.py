import numpy as np
import database as db
import math

from numpy import matlib as mtlb
def dataGeneration(nClust, nCoord, patNumb, N):
    # coordinates of clusters' centers:
    # Hba1c|BMI|Age|HOMA2-B|HOMA2-IR
    cntrCoord = np.array([[80.03, 27.45, 50.48, 56.71, 2.16], #SAID
                          [101.85, 28.86, 56.74, 47.64, 3.18], #SIDD
                          [54.07, 33.85, 65.25, 150.47, 5.54], #SIRD
                          [57.70, 35.71, 48.96, 95.03, 3.35], #MOD
                          [50.08, 27.94, 67.37, 86.59, 2.55]]) #MARD
    # downer borders of clusters:
    # Hba1c|BMI|Age|HOMA2-B|HOMA2-IR
    dwnBrdrs = np.array([[52, 22, 36, 23, 1.1], #SAID
                         [88, 26, 50, 25, 2.2], #SIDD
                         [45, 31, 60, 120, 3.7], #SIRD
                         [47, 32, 39, 74, 2.5], #MOD
                         [43, 26, 61, 70, 2.0]]) #MARD
    # upper borders of clusters:
    # Hba1c|BMI|Age|HOMA2-B|HOMA2-IR
    upBrdrs = np.array([[105, 31, 64, 80, 2.5], #SAID
                        [115, 32, 64, 60, 3.7], #SIDD
                        [57, 37, 72, 170, 5.9], #SIRD
                        [66, 39, 57, 115, 4.1], #MOD
                        [54, 30, 73, 105, 2.8]]) #MARD
    # calculation SD for all clusters:
    koef = 1.349
    SD = (upBrdrs - dwnBrdrs) / koef
    #calculation data for all clusters:
    allData = np.zeros([nCoord, N])
    for i in range(nCoord):
        l = 0
        r = 0
        for j in range(nClust):
            r += patNumb[j]
            allData[i, l : r] = np.random.normal(cntrCoord[j, i], SD[j, i], patNumb[j])
            for e in range(patNumb[j]):
                if allData[i, l + e] < dwnBrdrs[j, i]:
                    allData[i, l + e] = dwnBrdrs[j, i]
                if allData[i, l + e] > upBrdrs[j, i]:
                    allData[i, l + e] = upBrdrs[j, i]
            l = l + patNumb[j]
    return allData

def errorsGeneration(nCoord, N, M, dataWithoutErrors):
    erHOMA_B = db.slctRow('HOMA_errors', 'HOMA2_B')
    erHOMA_IR = db.slctRow('HOMA_errors', 'HOMA2_IR')
    # Hba1c|BMI|Age|HOMA2-B|HOMA2-IR
    errorPrm = [0.03, 0.02, 0.5, math.sqrt(erHOMA_B[2]), math.sqrt(erHOMA_IR[2])] # parameters of errors
    # errors generation:
    errors = np.zeros([M, nCoord, N])
    errorBMI = dataWithoutErrors[1, :] * errorPrm[1]
    for i in range(M):
        errors[i, 0, :] = np.random.normal(0, dataWithoutErrors[0, :] * errorPrm[0], N)
        for j in range(N):
            errors[i, 1, j] = np.random.uniform(-errorBMI[j], errorBMI[j])
        errors[i, 2, :] = np.random.uniform(-errorPrm[2], errorPrm[2], N)
        errors[i, 3, :] = np.random.normal(0, errorPrm[3], N)
        errors[i, 4, :] = np.random.normal(0, errorPrm[4], N)
    return errors

def main():
    nClust = 5 # the number of clusters
    nCoord = 5 # the number of coordinates
    k = 1 # the coefficient for patient's number
    # numbers of patients in clusters:
    patNumb = [577 * k, 1575 * k, 1373 * k, 1942 * k, 3513 * k]
    N = sum(patNumb)
    M = 1000 # the number of repeats
    dataWithoutErrors = dataGeneration(nClust, nCoord, patNumb, N)
    errors = errorsGeneration(nCoord, N, M, dataWithoutErrors)
    dataWithErrors = np.zeros([M, nCoord, N])
    for i in range(M):
        dataWithErrors[i, :, :] = dataWithoutErrors + errors[i, :, :]
    # np.save('dataWithoutErrors.npy', dataWithoutErrors)
    # np.save('dataWithErrors.npy', dataWithErrors)

if __name__ == "__main__":
    main()