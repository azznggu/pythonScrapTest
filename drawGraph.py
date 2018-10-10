##import matplotlib.animation as animation
#import matplotlib.style as style
#import time, sched
import matplotlib.pyplot as plt
import numpy as np
import random

class DrawGraph:
    #def __init__(self):
        #s = sched.scheduler(time.time, time.sleep)
        #plt.ion()
        #plt.show()
        
    def draw(list) :
            for x in range(len(list)) :
                #plt.plot(x, y, c = "blue")
                plt.scatter(x, list[x])
                plt.pause(1)
                #plt.draw()
            