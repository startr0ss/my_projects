import numpy as np
from numpy import matlib as mtlb
import win32com.client as w32
import database as db

def calculationOfHOMA(arrayIn):
    # Excel parameters:
    path = 'D:\Учеба\Python projects\diabetResearch\HOMA2Calculator Validation.xls'
    rngHOMA = ['F3:F314', 'H3:H314'] # HOMA2-B|HOMA2-IR
    # calculation of modal values for HOMA2-B and HOMA2-IR
    excel = w32.Dispatch("Excel.Application")
    wb = excel.Workbooks.Open(path)
    sh = wb.Sheets(4)
    for i, vl in enumerate(arrayIn):
        sh.Cells(i + 3, 1).Value = vl[0]
        sh.Cells(i + 3, 2).Value = vl[1]
    arrayOut = np.zeros((2, np.size(arrayIn, axis=0)))
    arrayOut[0, :] = [i[0].value for i in sh.Range(rngHOMA[0])]
    arrayOut[1, :] = [i[0].value for i in sh.Range(rngHOMA[1])]
    wb.Save()
    wb.Close()
    return np.transpose(arrayOut)

def generationOfGlucAndCpept(gluc, cPept):
    szGluc = np.size(gluc)
    szCPept = np.size(cPept)
    arrayIn = np.zeros((2, szGluc * szCPept))
    for i in range(szGluc):
        arrayIn[0, (i * szCPept) : ((i + 1) * szCPept)] = mtlb.repmat(gluc[i], 1, szCPept)
        arrayIn[1, :] = mtlb.repmat(cPept, 1, szGluc)
    return np.transpose(arrayIn)

def main():
    # generation of modal values for glucose and C-peptide:
    glucBase = np.arange(6, 12.5, 0.5)
    cPeptBase = np.arange(0.2, 2.6, 0.1)
    modalArrayIn = generationOfGlucAndCpept(glucBase, cPeptBase)
    modalArrayOut = calculationOfHOMA(modalArrayIn)
    cv = [0.01, 0.04] # glucose|C-peptide
    M = 1000  # the number of repeats
    HOMA2_B = np.zeros((np.size(modalArrayIn, axis=0), M))
    HOMA2_IR = np.zeros((np.size(modalArrayIn, axis=0), M))
    for i in range(M):
        gluc = glucBase + np.random.normal(0, glucBase * cv[0], np.size(glucBase))
        cPept = cPeptBase + np.random.normal(0, cPeptBase * cv[1], np.size(cPeptBase))
        # requirements of HOMA2Calculator:
        for j in range(np.size(cPept)):
            if cPept[j] < 0.2:
                cPept[j] = 0.2
            if cPept[j] > 2.5:
                cPept[j] = 2.5
        arrayIn = generationOfGlucAndCpept(gluc, cPept)
        arrayOut = calculationOfHOMA(arrayIn)
        HOMA2_B[:, i] = arrayOut[:, 0]
        HOMA2_IR[:, i] = arrayOut[:, 1]
    modalHOMA2_B = modalArrayOut[:, 0]
    modalHOMA2_IR = modalArrayOut[:, 1]
    modalHOMA2_B = np.transpose(mtlb.repmat(modalHOMA2_B, M, 1))
    modalHOMA2_IR = np.transpose(mtlb.repmat(modalHOMA2_IR, M, 1))
    errorsHOMA2_B = HOMA2_B - modalHOMA2_B
    errorsHOMA2_IR = HOMA2_IR - modalHOMA2_IR
    m2ErrorHOMA2_B = np.sqrt(np.sum(pow(errorsHOMA2_B, 2), axis=0) / np.size(errorsHOMA2_B, axis=0))
    m2ErrorHOMA2_IR = np.sqrt(np.sum(pow(errorsHOMA2_IR, 2), axis=0) / np.size(errorsHOMA2_IR, axis=0))
    # work with database:
    valuesB = [min(m2ErrorHOMA2_B), sum(m2ErrorHOMA2_B) / M, max(m2ErrorHOMA2_B)]
    valuesIR = [min(m2ErrorHOMA2_IR), sum(m2ErrorHOMA2_IR) / M, max(m2ErrorHOMA2_IR)]
    nameTbl = 'HOMA_errors'
    checkTable = db.checkTable(nameTbl)
    if checkTable == None:
        db.crtTable(nameTbl)
        db.insertHOMA(nameTbl, 'HOMA2_B', valuesB)
        db.insertHOMA(nameTbl, 'HOMA2_IR', valuesIR)
    else:
        db.updateTable(nameTbl, 'HOMA2_B', valuesB)
        db.updateTable(nameTbl, 'HOMA2_IR', valuesIR)
    db.showTable(nameTbl)

if __name__ == "__main__":
    main()