import numpy as np
import time
import threading
from matplotlib import pyplot as plt
from matplotlib import animation

isRunning = True

#Below is the data generating part

imageArr = np.ones((255, 255))

#Below is the plotting part

ScaleMax = 255 * 2 + 80
ScaleMin = 0

fig = plt.figure()
im = plt.imshow(imageArr, cmap = "gray", vmin = ScaleMin, vmax = ScaleMax)
plt.colorbar(im)


# Calculation function
def Calculation() :
    while(isRunning) :
        for i in range(0, len(imageArr)) :
            for j in range(0, len(imageArr[i])) :
                imageArr[i][j] = i + j + np.random.random() * 80
                #imageArr[i][j] = np.random.random() * ScaleMax
#        print(imageArr)
        time.sleep(0.15)
    return

# Animation function
def Animate(i) :
   # data = np.random.random((255, 255));
    im.set_array(imageArr)
    return [im]

#Create the calculation thread
hCalculation = threading.Thread(target = Calculation)
hCalculation.start()

anim = animation.FuncAnimation(fig, Animate, frames = 200, interval = 30, blit = True)
plt.show()
isRunning = False