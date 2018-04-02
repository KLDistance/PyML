import numpy as np
import matplotlib as plt
import matplotlib.pyplot as pyplt
from mpl_toolkits.mplot3d import Axes3D
'''
The superivsed learning is that, given the "right" answer for each
example in the data

For the Regression problem, its important to predict real-valued output.
That is to classify, discrete-valued output.


'''

'''
How to operate the array and matrix:
x = np.array([1, 2, 3, 4]);
y = 3;
print(x * y);
print();

p1 = np.mat([
    [1, 2, 3],
    [2, 3, 4],
    [4, 4, 4]
]);
p2 = np.mat(
    [
        [2, 3, 2],
        [1, 2, 1],
        [1, 1, 1]
    ]
);
print(p1 * p2);
'''

'''
Training set -> Learning algorithm -> h as a function
Using h, input -> output estimation

linear regression == univalue regression
Hypothesis: h(x) = theta0 + theta1 * x
'''
samples = np.array([
    [1.00, 3.00],
    [1.09, 2.91],
    [1.01, 3.12],
    [2.41, 6.98],
    [4.21, 13.38],
    [8.13, 25.25], 
    [6.23, 18.91]
])

sampleNum = len(samples)

# Range of slope and intercepts
initSlope = -7
initIntercept = -40

slopeStep = 0.4
interceptStep = 2

slopeIterTimes = 40
interceptIterTimes = 40

contourField = np.zeros((slopeIterTimes * interceptIterTimes))
contourX = np.zeros((slopeIterTimes * interceptIterTimes))
contourY = np.zeros((slopeIterTimes * interceptIterTimes))

# Cost function
def costFunction(presSlope, presIntercept) :
    presErrorSquare = 0
    for i in range(0, sampleNum, 1) :
        presIdeal = presSlope * samples[i][0] + presIntercept
        presErrorSquare += (samples[i][1] - presIdeal) ** 2
    return presErrorSquare / (2 * sampleNum)

# Assign the values into arrays
for tmpSlopeIter in range(0, slopeIterTimes, 1) :
    for tmpInterceptIter in range(0, interceptIterTimes, 1) :
        contourField[tmpSlopeIter * interceptIterTimes + tmpInterceptIter] = costFunction(tmpSlopeIter * slopeStep + initSlope, tmpInterceptIter * interceptStep + initIntercept)
        contourX[tmpSlopeIter * interceptIterTimes + tmpInterceptIter] = tmpInterceptIter
        contourY[tmpSlopeIter * interceptIterTimes + tmpInterceptIter] = tmpSlopeIter



fig = pyplt.figure()
ax = Axes3D(fig)

ax.scatter(contourX, contourY, contourField)
ax.set_xlabel('Intercept')
ax.set_ylabel('Slope')
ax.set_zlabel('Cost')
pyplt.show()

