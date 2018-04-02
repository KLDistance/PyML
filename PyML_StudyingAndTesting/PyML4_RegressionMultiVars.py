'''
New hypothesis :
h(x) = theta0 + theta1 * x1 + theta2 * x2 + theta3 * x3 + ...
h(x) = THETA & T * X
'''

import numpy as np
from matplotlib import pyplot as plt
import math
import time

'''
Here we need to allocate 4 factors :
1. a -> 0
2. b -> 1
3. c -> 2
4. d -> 3
5. e -> 4
'''
'''
datasetY = np.transpose(datasetX)

for i in range(0, 25, 1) :
    datasetY[0, i] = datasetY[0, i] * 2 + np.random.random() * 7

print(datasetY) 

datasetY = np.mat(
    [
    [   4.42800398  10.3144466   15.80395846  18.42413176   6.81771894
        24.81347842  24.06039274  16.71119221   5.53617172   6.80722919
        12.59549339   8.73986991  14.26682156  12.59859558  11.25574642
        30.04612664  21.01195388  24.08545196   1.22389679  19.68052914
        43.37828133  30.29127923  48.07054495  19.85536825  33.28949832
    ]
    ]
)
'''
datasetX = np.mat([
    [1.324, 4.235, 5.201, 8.231, 2.001],
    [11.111, 10.928, 5.928, 2.091, 3.101],
    [3.213, 2.521, 5.342, 3.429, 4.111],
    [14.341, 7.677, 9.081, 0.013, 9.231],
    [18.32, 13.333, 21.31, 8.989, 13.414]
])

datasetY = np.mat(
    [[   4.42800398, 24.81347842, 12.59549339, 30.04612664, 43.37828133    ]]
)
# Dimension of parameter set should equal to the col number of 
initParaSet = np.mat(
    [[1, 1, 1, 1, 1]]
)

rowNum = datasetX.shape[0]
colNum = datasetX.shape[1]

# TmpParaSet used in the MatGradDescOnce function
tmpParaSet = np.zeros([1, rowNum])
for i in range(0, rowNum) :
    tmpParaSet[0, i] = initParaSet[0, i]

lRate = 0.002
limitIterNum = 1000
actualIterNum = 0
errorTolerant = 0.000001

def MatGradDescOnce(equParaSet) : 
    global tmpParaSet
    for i in range(0, colNum) :
        deltaSum = 0
        for j in range(0, rowNum) :
            calcSum = 0
            for k in range(0, rowNum) :
                calcSum += (equParaSet[0, k] * datasetX[k, i])
            deltaSum += ((calcSum - datasetY[0, i]) * datasetX[j, i])
        tmpParaSet[0, i] = equParaSet[0, i] - deltaSum * lRate / colNum
    return

def MatGradDesc() :
    global tmpParaSet, actualIterNum
    AfterParaSet = np.zeros([1, rowNum])
    for i in range(0, rowNum) : 
        AfterParaSet[0, i] = tmpParaSet[0, i]
    while(actualIterNum < limitIterNum) :
        MatGradDescOnce(AfterParaSet)
        actualIterNum += 1
        judge = False
        for j in range(0, rowNum) :
            if(AfterParaSet[0, j] == 0 or\
                 np.abs(AfterParaSet[0, j] - tmpParaSet[0, j]) / AfterParaSet[0, j] < errorTolerant) : 
                judge = True
                break
        if (judge == True) : break
        for k in range(0, rowNum) :
            AfterParaSet[0, i] = tmpParaSet[0, i]

MatGradDesc()
print(tmpParaSet)
print("Iteration time:", actualIterNum)

