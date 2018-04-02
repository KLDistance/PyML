import numpy as np
import time
import threading
from matplotlib import pyplot as plt
from matplotlib import animation

isRunning = True

fig = plt.figure()
data = []
data.append(np.random.random((255, 255)))
im = plt.imshow(data[0], cmap = "gray")

# Calculation function
def Calculation() :
    while(isRunning) :
        data[0] = np.random.random((255, 255))
        time.sleep(0.05)
    return

# Animation function
def Animate(i) :
   # data = np.random.random((255, 255));
    im.set_array(data[0])
    return [im]

#Create the calculation thread
hCalculation = threading.Thread(target = Calculation)
hCalculation.start()

anim = animation.FuncAnimation(fig, Animate, frames = 200, interval = 30, blit = True)
plt.show()
isRunning = False