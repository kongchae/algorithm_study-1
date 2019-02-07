# 1.8
# 0행렬 : M * N 행렬의 한 원소가 0일 경우,
# 해당 원소가 속한 행과 열의 모든 원소를 0으로 설정하는 알고리즘을 작성하라.

import numpy as np

# y = np.array(list('ABCDE'*5)).reshape(5,5)
# print(y)
#
# d = np.array([(1,2,3),(4,5,6)], dtype=int)
#
# print(d)

a = np.array([(0,2,3),(4,5,6),(7,8,9)]) # (0,0,0),(0,5,6),(0,8,9)
b = np.array([(1,0),(3,4),(5,6),(7,8)]) #(0,0),(3,0),(5,0),(7,0)
# print(a)
# print(b)

def matrix(arr):
    nr = 'null' #num row
    nc = 'null' #num column
    for i in range(len(arr)): #row
        for j in range(len(arr[i])): #column
            if arr[i][j] == 0:
                nr = i
                nc = j


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == nr:





matrix(a)
matrix(b)