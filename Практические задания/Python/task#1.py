import numpy as np

n1 = 10 ** 1
brdr = 10
array1 = np.zeros(n1)
array2 = np.zeros(n1)
array1 = [(i + 1) for i, _ in enumerate(array1)]
array2 = np.random.uniform(-brdr, brdr, n1)
sum1 = array1 + array2
subtract1 = array1 - array2
multiply1 = array1 * array2 # поэлементно
division1 = array1 / array2 # поэлементно
n2 = 4
array3 = np.zeros((n2, n1))
array4 = np.zeros((n2, n1))
for i in range(n2):
    array3[i, :] = [(j + 1 + (i * 10)) for j, _ in enumerate(array3[i, :])]
    array4[i, :] = np.random.uniform(-brdr, brdr, n1)
sum2 = array3 + array4
subtract2 = array3 - array4
multiply2 = array3 * array4 # поэлементно
division2 = array3 / array4 # поэлементно