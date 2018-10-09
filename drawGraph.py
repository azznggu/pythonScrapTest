import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.style as style
import time, sched
import random

class DrawGraph:
    def __init__(self):
        s = sched.scheduler(time.time, time.sleep)
        plt.ion()
        plt.show()

    def draw(self) :
        figure = plt.figure()
        plt.subplot(111)
        plt.title("plot chart")

        #ax = figure.add_subplot(111)
        for x in range(1,100) :
            y = random.randint(1,10)
            plt.plot(x, y, linestyle='solid')
            plt.scatter(x, y)
            plt.pause(0.1)
            plt.draw()
        #plt.show()
            

        
drawGraph = DrawGraph()
drawGraph.draw()      


