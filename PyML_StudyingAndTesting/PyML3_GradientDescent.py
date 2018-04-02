'''
Gradient descent :
thetaj = thetaj - alpha * PDF(J(theta0, theta1))[thetaj];

Linear Regression :
h(x) = theta0 + theta1 * x

combination:
1. For theta0 PDF to J0 = (1/m) Σ(hx - y)
2. For theta1 PDF to J1 = (1/m) Σ[(hx - y) * x]

For linear function, they are always convex functions and the contour figures are always bow-shaped

This is a kind of "Batch" Gradient Descent :
Each step of gradient descent uses all the training examples;
'''
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
import time
import threading

dataSetX = np.array([
    1.00,
    1.09,
    1.01,
    2.41,
    4.21,
    8.13,
    6.32,
    14.0,
    9.30,
    2.43,
    5.21,
    9.39,
    11.98,
    2.98,
    7.93,
    4.48
])

dataSetY = np.array([
    3.00,
    2.91,
    3.12,
    6.98,
    13.38,
    25.25,
    18.91,
    31.0,
    34.0,
    8.72,
    13.13,
    29.01,
    28.03,
    6.13,
    25.19,
    14.92
])

sampleNum = len(dataSetX)

initSlope = -10.0
initIntercept = 20.0

presSlope = initSlope
presIntercept = initIntercept

lRate = 0.001
limitIterNum = 1000
actualIterNum = 0
errorTolerant = 0.0001

# Predefine the plots objects
scaleMin = -5
scaleMax = 35
lineXInit = 0
lineXEnd = 15
lineYInit = 0
lineYEnd = 0

lineColor = 'cyan'

fig = plt.figure()
im1 = plt.scatter(dataSetX, dataSetY)
im2 = None


# Execute Gradient Descent once
def GradDescOnce(presIntercept, presSlope) :
    interceptSum = 0.0
    slopeSum = 0.0
    for i in range(0, sampleNum, 1) :
        tmp = presSlope * dataSetX[i] + presIntercept - dataSetY[i]
        interceptSum += tmp
        slopeSum += (tmp * dataSetX[i])
    afterIntercept = presIntercept - interceptSum * lRate / sampleNum
    afterSlope = presSlope - slopeSum * lRate / sampleNum
    return afterIntercept, afterSlope

# Execute Gradient Descent within limiting times
def GradDesc(slope = None, intercept = None) : 
    global presIntercept, presSlope, actualIterNum, lineColor
    lastIntercept = presIntercept
    lastSlope = presSlope
    while(actualIterNum < 1000) :
        presIntercept, presSlope = GradDescOnce(lastIntercept, lastSlope)
        print('Intercept: ', presIntercept, 'Slope: ', presSlope)
        time.sleep(0.005)
        actualIterNum += 1
        if np.abs(lastSlope - presSlope) < errorTolerant :
            if presIntercept == 0 or np.abs(lastIntercept - presIntercept) / lastIntercept < errorTolerant : break
        lastIntercept = presIntercept
        lastSlope = presSlope
    print("Approach complete!")
    lineColor = 'green'
    return

# Draw the plot with animation
def DrawAnimation(i) :
    im1 = plt.scatter(dataSetX, dataSetY, color = "red")
    lineYInit = lineXInit * presSlope + presIntercept
    lineYEnd = lineXEnd * presSlope + presIntercept
    im2 = plt.plot([lineXInit, lineXEnd], [lineYInit, lineYEnd], color = lineColor)
    return [im1, im2]

hGradDesc = threading.Thread(target = GradDesc)
anim = animation.FuncAnimation(fig, DrawAnimation, frames = 50, interval = 100, blit = False)

hGradDesc.start()
plt.show()



